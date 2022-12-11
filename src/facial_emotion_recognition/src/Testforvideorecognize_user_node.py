#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import *

from facial_emotion_recognition.srv import video_detect_user
from sensor_msgs.msg import Image

# #i messaggi correttamente riconosciuti verranno mandati a rasa
# pub1 = rospy.Publisher('text2answer', RecognizedSpoke, queue_size=10)
# #i messaggi non correttamente riconosciuti verranno notificati
# pub2 = rospy.Publisher('toSpeech', String, queue_size=10)

# Init node
rospy.init_node('recognize_user', anonymous=True)

#function to recognize user with both audio and video
def recognize_user(text_to_send):
    # rospy.wait_for_service('audio_user_server')
    rospy.wait_for_service('video_user_server')
    try:
        # obtain_audio_id = rospy.ServiceProxy('audio_user_server', #funz per ottenere id dell audio)
        # id_voice = obtain_audio_id()
        # print("id voice:", id_voice)
        obtain_video_id = rospy.ServiceProxy('video_user_server', video_detect_user)
        id_face = obtain_video_id()
        print("id face:", id_face)
        # if(id_face == id_voice):
        #     #l'utente è stato correttamente riconosciuto quindi devo inviare tutto a rasa
        #     pub1.publish(text_to_send)
        # else:
        #     #l'utente non è stato correttamente riconosciuto
        #     pub2.publish("I can't recognize you")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)

    


def listener():
    rospy.Subscriber("image", Image, recognize_user)
    rospy.spin()

if __name__ == '__main__':
    listener()