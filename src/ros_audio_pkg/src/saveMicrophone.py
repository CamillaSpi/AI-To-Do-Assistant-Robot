#!/usr/bin/python3
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
count = 10
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