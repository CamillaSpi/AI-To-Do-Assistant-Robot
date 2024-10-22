#!/usr/bin/python3

"""
This is a Python script that uses the ROS framework, the speech_recognition library, 
and the ros_audio_pkg package to perform speech recognition on audio data.
The script creates publisher objects that will be used to publish on the received audio, interpretedtext and tospeech topics.
The script starts when voice data are received; the callback function, called when new audio data is received, 
uses the Recognizer object to recognize speech in the audio data using Google's speech recognition service.
The audio received is published on recivedAudio, used by speaker identification, the text recognized is published
on interpretedText topic and will be elaborated by the recognize user node in conductor. At the end, if the text
of the audio data is not recognized, a publish on toSpeech topic is done to let the bot say this sentence.
"""


import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

from speech_recognition import AudioData
import speech_recognition as sr
import time

# Initialize a Recognizer
r = sr.Recognizer()

# Init node
rospy.init_node('speech_recognition', anonymous=True)
pub1 = rospy.Publisher('RecivedAudio', Int16MultiArray, queue_size=1) #publish the recived audio
pub2 = rospy.Publisher('InterpretedText', String, queue_size=1) #publish the recognized text
pubSpeech = rospy.Publisher('toSpeech', String,queue_size=1)

def callback(audio):
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    
    try:
        
        spoken_text= r.recognize_google(audio_data,language="it-IT")
        rospy.loginfo("Google Speech Recognition pensa tu abbia detto: " + spoken_text)
        
        pub1.publish(audio)
        time.sleep(0.2)
        pub2.publish(spoken_text.lower())
    except sr.UnknownValueError:
        rospy.loginfo("Google Speech Recognition non riesce a capire da questo file audio")
        pubSpeech.publish("Scusa, puoi ripetere")
    except sr.RequestError as e:
        rospy.loginfo("Could not request results from Google Speech Recognition service; {0}".format(e))

def listener():
    rospy.Subscriber("mic_data", Int16MultiArray, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()