#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, Bool
import numpy as np

import time
import speech_recognition as sr

pub = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)
rospy.init_node('voice_detection_node', anonymous=True)


global old_bool
global stop_listening
old_bool = True

# this is called from the background thread
def callback(recognizer, audio):
    data = np.frombuffer(audio.get_raw_data(), dtype=np.int16) * 10
    data_to_send = Int16MultiArray()
    data_to_send.data = data
    pub.publish(data_to_send)

# Initialize a Recognizer
r = sr.Recognizer()

# Audio source
m = sr.Microphone(device_index=None,
                    sample_rate=16000,
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
        else:
            stop_listening = r.listen_in_background(m, callback)
        old_bool = msg.data
        

pub2 = rospy.Subscriber('thereIsPerson', Bool,rcv_person)

rospy.spin()