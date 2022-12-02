#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

from speech_recognition import AudioData
import speech_recognition as sr

# Initialize a Recognizer
r = sr.Recognizer()

# Init node
rospy.init_node('speech_recognition', anonymous=True)
pub1 = rospy.Publisher('voice_data', Int16MultiArray, queue_size=10)
pub2 = rospy.Publisher('spoken_text', String, queue_size=10)

# this is called from the background thread
def callback(audio):
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)

    try:
        spoken_text= r.recognize_google(audio_data)
        print("Google Speech Recognition pensa tu abbia detto: " + spoken_text)
        pub1.publish(audio) # Publish audio only if it contains words
        pub2.publish(spoken_text)
    except sr.UnknownValueError:
        print("Google Speech Recognition non riesce a capire da questo file audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def listener():
    rospy.Subscriber("mic_data", Int16MultiArray, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()