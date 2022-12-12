#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from ros_audio_pkg.msg import RecognizedSpoke
from pepper_nodes.srv import *
from ros_audio_pkg.srv import idLabel
from facial_emotion_recognition.srv import video_detect_user

#i messaggi correttamente riconosciuti verranno mandati a rasa
pub1 = rospy.Publisher('text2answer', RecognizedSpoke, queue_size=10)
#i messaggi non correttamente riconosciuti verranno notificati
pub2 = rospy.Publisher('toSpeech', String, queue_size=10)

# Init node
rospy.init_node('recognize_user', anonymous=True)
rospy.wait_for_service('voiceLabelServices')
rospy.wait_for_service('video_user_server')
obtain_audio_id = rospy.ServiceProxy('voiceLabelServices', idLabel)
obtain_video_id = rospy.ServiceProxy('video_user_server', video_detect_user)

#function to recognize user with both audio and video
def recognize_user(text_to_send):
    try:
        id_face = obtain_video_id().answer
        print("id face:", id_face)
        id_voice = obtain_audio_id().id
        print("id voice:", id_voice)
        if(id_voice in id_face):
            #l'utente è stato correttamente riconosciuto quindi devo inviare tutto a rasa
            toSend = RecognizedSpoke()
            toSend.msg = text_to_send.data
            toSend.id = id_voice
            pub1.publish(toSend)
            print('ti riconosco')
        else:
            print('non ti  riconosco')
        pass
            #l'utente non è stato correttamente riconosciuto
            # pub2.publish("I can't recognize you")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)

    


def listener():
    rospy.Subscriber('InterpretedText', String, recognize_user)
    rospy.spin()

if __name__ == '__main__':
    listener()