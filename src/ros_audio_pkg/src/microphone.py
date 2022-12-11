#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16MultiArray
import numpy as np
import pyaudio
#pyaudo pu; funzionare anche nn in streaming, in questo caso attraverso un ciclo while andiamo a prendere i dati quanod necessario.

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
WIN_SIZE_SEC = 0.03
CHUNK = int(WIN_SIZE_SEC * RATE)

from time import sleep

def publisher():
    pub = rospy.Publisher('mic_data', Int16MultiArray, queue_size=10)
    rospy.init_node('microphone_node', anonymous=True)

    # Init recorder
    audio = pyaudio.PyAudio()
    # in data contiene tutte le info che ci interessano. PyAudio ci restituisce un array in int16, 
    def callback(in_data, frame_count, time_info, status ):
        # Waveform read
        data = np.frombuffer(in_data, dtype=np.int16)
        data_to_send = Int16MultiArray()
        data_to_send.data = data
        
        pub.publish(data_to_send)

        return in_data, pyaudio.paContinue

    # Start recording

    # List microphone index
    # import sounddevice as sd
    # sd.query_devices()
    # cosi facendo andiamo a eseguire questa funzione ogni qualvolta e disponibile un file audio
    stream = audio.open(input_device_index=None,        
                        format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        stream_callback=callback)
    
    rospy.spin()

    # Close the stream
    stream.close()
    audio.terminate()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass