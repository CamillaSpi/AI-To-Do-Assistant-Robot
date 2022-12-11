#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from ros_audio_pkg.msg import RecognizedSpoke
from pepper_nodes.srv import *
from ros_audio_pkg.srv import idLabel

#i messaggi correttamente riconosciuti verranno mandati a rasa
pub1 = rospy.Publisher('text2answer', RecognizedSpoke, queue_size=10)
#i messaggi non correttamente riconosciuti verranno notificati
pub2 = rospy.Publisher('toSpeech', String, queue_size=10)

# Init node
rospy.init_node('recognize_user', anonymous=True)
rospy.wait_for_service('voiceLabelServices')
obtain_audio_id = rospy.ServiceProxy('voiceLabelServices', idLabel)

#function to recognize user with both audio and video
def recognize_user(text_to_send):
    #rospy.wait_for_service('video_user_server')
    try:
        id_voice = obtain_audio_id()
        print("id voice:", id_voice)
        # obtain_video_id = rospy.ServiceProxy('video_user_server', video_detect_user)
        # id_face = obtain_video_id()
        # print("id face:", id_face)
        # if(id_face == id_voice):
        #     #l'utente è stato correttamente riconosciuto quindi devo inviare tutto a rasa
        #     pub1.publish(text_to_send)
        # else:
        #     #l'utente non è stato correttamente riconosciuto
        #     pub2.publish("I can't recognize you")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)

    


def listener():
    rospy.Subscriber('InterpretedText', String, recognize_user)
    rospy.spin()

if __name__ == '__main__':
    listener()