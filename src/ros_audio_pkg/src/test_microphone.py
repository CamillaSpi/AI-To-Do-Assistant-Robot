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
data_list = []
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/nando.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/nando2.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/nando3.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)

data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/frase1_vito.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/frase2_vito.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/frase3_vito.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)

data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/frase1.mp3')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/frase2.mp3')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/frase3.mp3')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)

data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/hiPepperMattiaUSB.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/adRuninGymTomMattiaUSB.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)
data, x = librosa.load('/home/nando-child/Scrivania/DefinitivoCog/src/ros_audio_pkg/rec_audio/addStudyInUniversityMattiaUSB.m4a')
data = int16 = (data * 32767).astype(np.int16)
data_list.append(data)


from time import sleep


if __name__ == '__main__':
    try:
        pub = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)
        sleep(2)
        rospy.init_node('microphone_node', anonymous=True)
        for data in data_list:
            data_to_send = Int16MultiArray()
            data_to_send.data = data

            pub.publish(data_to_send)
            sleep(1)


    except rospy.ROSInterruptException:
        pass