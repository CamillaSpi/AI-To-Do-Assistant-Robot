#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

from speech_recognition import AudioData
import speech_recognition as sr
from ros_audio_pkg.msg import AudioAndText
#from datetime import datetime

# Initialize a Recognizer
r = sr.Recognizer()

# Init node
rospy.init_node('speech_recognition', anonymous=True)
pub1 = rospy.Publisher('AudioAndText', AudioAndText, queue_size=10)

# this is called from the background thread
def callback(audio):
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    
    try:

        #t1 = datetime.now()
        spoken_text= r.recognize_google(audio_data)
        print("Google Speech Recognition pensa tu abbia detto: " + spoken_text)
        #t2 = datetime.now()
        #delta = t2-t1
        #print('inference time ' , delta.total_seconds())
        audioAndText = AudioAndText()
        audioAndText.spoken_text = spoken_text
        audioAndText.audioData = audio.data
        pub1.publish(audioAndText)
    except sr.UnknownValueError:
        print("Google Speech Recognition non riesce a capire da questo file audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def listener():
    rospy.Subscriber("mic_data", Int16MultiArray, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()