#!/usr/bin/python3

"""
This is a Python script that uses the ROS framework, the speech_recognition library, and the ros_audio_pkg package to save audio data.
The script then creates a variable count initialized to 0, it will be used to name the files. 
The script initializes a ROS node and creates a publisher object that will be used to publish the audio and text data to a topic.
This script was used only in test phase.
"""

import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

from speech_recognition import AudioData
import speech_recognition as sr
from ros_audio_pkg.msg import AudioAndText
import os
#from datetime import datetime

# Initialize a Recognizer
r = sr.Recognizer()

# Init node
rospy.init_node('speech_recognition', anonymous=True)
pub1 = rospy.Publisher('AudioAndText', AudioAndText, queue_size=10)
count = 0
# this is called from the background thread
def callback(audio):
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    rospy.loginfo('salvo file audio')
    with open(os.path.dirname(__file__)+"/../audioSample/"+str(count)+"_audio_file.wav" , 'wb') as file:
        file.write(audio_data.get_wav_data())
    rospy.loginfo('salvato!!')



def listener():
    rospy.Subscriber("mic_data", Int16MultiArray, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()