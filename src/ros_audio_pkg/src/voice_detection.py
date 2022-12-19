#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, Bool
import numpy as np

import time
import speech_recognition as sr
import pyaudio

pyaudio_instance = pyaudio.PyAudio()


pub = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)
rospy.init_node('voice_detection_node', anonymous=True)


global old_bool
global stop_listening
old_bool = True


# find the index of respeaker usb device
def find_device_index():
    found = -1
    for i in range(pyaudio_instance.get_device_count()):
        dev = pyaudio_instance.get_device_info_by_index(i)
        name = dev['name'].encode('utf-8')
        if name.lower().find(b'respeaker') >= 0 and dev['maxInputChannels'] > 0:
            found = i
            break
    return found

device_index = find_device_index()
if device_index < 0:
    print('No ReSpeaker USB device found')
    num_microphone = 2
    # num_microphone = 1
else:
    print('Find ReSpeaker USB Device')
    num_microphone = 4


# this is called from the background thread
def callback(recognizer, audio):
    data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
    max = np.sum(data[0::num_microphone])
    toSend = data[0::num_microphone]
    #though this for loop we search for the microphone with the max summed value, this should correspond to the principal microphone where the speaker is talking
    for x in range(1,num_microphone): 
        tmp = np.sum(data[x::num_microphone])
        if max < tmp:
            max = tmp 
            toSend = data[x::num_microphone]

    data_to_send = Int16MultiArray()
    data_to_send.data = toSend*3
    pub.publish(data_to_send)

# Initialize a Recognizer
r = sr.Recognizer()

# Audio source
m = sr.Microphone(device_index=None,
                    sample_rate=16000*num_microphone,
                    chunk_size=1024)

# Calibration within the environment
# we only need to calibrate once, before we start listening
# necessario per andare a calibrare il segnale.
# se c'e molto rumore non riesce a comrpedenre bene, vado quindi a sistemare questa cosa
print("Calibrating...")
with m as source:
    r.adjust_for_ambient_noise(source,duration=3)  
print("Calibration finished")

# start listening in the background
# `stop_listening` is now a function that, when called, stops background listening
print("Recording...")
stop_listening = r.listen_in_background(m, callback)


def rcv_person(msg):
    global old_bool
    global stop_listening
    if msg.data != old_bool:
        if not msg.data:
            stop_listening()
            print('stop ascolto')
        else:
            stop_listening = r.listen_in_background(m, callback)
            print('asolto')
        old_bool = msg.data
        

pub2 = rospy.Subscriber('isListening', Bool,rcv_person)

rospy.spin()