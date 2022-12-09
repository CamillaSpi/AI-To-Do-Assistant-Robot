#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16MultiArray
import numpy as np
import os
import librosa
#pyaudo pu; funzionare anche nn in streaming, in questo caso attraverso un ciclo while andiamo a prendere i dati quanod necessario.

CHANNELS = 1
RATE = 16000
WIN_SIZE_SEC = 0.03
CHUNK = int(WIN_SIZE_SEC * RATE)
from scipy.io import wavfile
print(os.path.abspath(os.getcwd()))
data, x = librosa.load('/home/nando/Desktop/DefinitivoCog/DefinitivoCog/src/ros_audio_pkg/test.wav')
data = int16 = (data * 32767).astype(np.int16)
from time import sleep


if __name__ == '__main__':
    try:
        
        pub = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)
        rospy.init_node('microphone_node', anonymous=True)
        data_to_send = Int16MultiArray()
        data_to_send.data = data

        pub.publish(data_to_send)



    except rospy.ROSInterruptException:
        pass