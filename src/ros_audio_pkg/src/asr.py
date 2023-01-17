#!/usr/bin/python3
import rospy
from std_msgs.msg import Int16MultiArray, String
import numpy as np

from speech_recognition import AudioData
import speech_recognition as sr
from ros_audio_pkg.msg import AudioAndText
import time
#from datetime import datetime

# Initialize a Recognizer
r = sr.Recognizer()

# Init node
rospy.init_node('speech_recognition', anonymous=True)
pub1 = rospy.Publisher('RecivedAudio', Int16MultiArray, queue_size=10) #publish the recived audio
pub2 = rospy.Publisher('InterpretedText', String, queue_size=10) #publish the recognized text
pubSpeech = rospy.Publisher('toSpeech', String,queue_size=10)

# this is called from the background thread
def callback(audio):
    data = np.array(audio.data,dtype=np.int16)
    audio_data = AudioData(data.tobytes(), 16000, 2)
    
    try:
        #t1 = datetime.now()
        spoken_text= r.recognize_google(audio_data,language="it-IT")
        rospy.loginfo("Google Speech Recognition pensa tu abbia detto: " + spoken_text)
        #t2 = datetime.now()
        #delta = t2-t1
        #rospy.loginfo('inference time ' , delta.total_seconds())
        #audioAndText = AudioAndText()
        #audioAndText.spoken_text = spoken_text
        #audioAndText.audioData = audio.data
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