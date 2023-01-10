#!/usr/bin/python3
import rospy
from std_msgs.msg import String,Bool,Int16
import numpy as np
from ros_audio_pkg.msg import RecognizedSpoke
from pepper_nodes.srv import *
from ros_audio_pkg.srv import idLabel,Registration
from face_recognition.srv import video_detect_user
import time

#i messaggi correttamente riconosciuti verranno mandati a rasa
pub1 = rospy.Publisher('text2answer', RecognizedSpoke, queue_size=10)
#i messaggi non correttamente riconosciuti verranno notificati
pub2 = rospy.Publisher('toSpeech', String, queue_size=10)

pub_recogizer_node = rospy.Publisher('startRegistration', Bool, queue_size=10)


natural_learning_voice = rospy.Publisher('naturalLearningVoice', Int16, queue_size=10)
natural_learning_face = rospy.Publisher('naturalLearningFace', Int16, queue_size=10)

# Init node
rospy.init_node('recognize_user', anonymous=True)
rejection_threshold = 0.7
rospy.wait_for_service('voiceLabelServices')
rospy.wait_for_service('video_user_server')
rospy.wait_for_service('voiceRegistrationService')
obtain_audio_prob = rospy.ServiceProxy('voiceLabelServices', idLabel)
obtain_video_prob = rospy.ServiceProxy('video_user_server', video_detect_user)
startVoiceRegistration = rospy.ServiceProxy('voiceRegistrationService', Registration)



#function to recognize user with both audio and video
def recognize_user(text_to_send):
    try:

        id_face_prob = obtain_video_prob().answer
        faces_stride = id_face_prob.layout.dim[0].stride
        id_face_prob_arr = np.asarray(id_face_prob.data)
        print("values faces: ", id_face_prob_arr )
        print("faces_stride", faces_stride)

        id_voice_prob = obtain_audio_prob().prob_voices
        id_voice_prob_arr = np.asarray(id_voice_prob.data)
        print("value voices", id_voice_prob_arr)
        
        
        start = 0
        max = 0
        id_max = -1
        
        while start != len(id_face_prob_arr):
            stop = start + faces_stride
            sum = np.sum([id_voice_prob_arr*0.40,id_face_prob_arr[start:stop]*0.60], axis = 0)
            print(sum)
            if(max < np.max(sum)):
                max = np.max(sum)
                id_max = np.argmax(sum)
            start = stop
        print("id_max",id_max,"max", max)
        if(max>rejection_threshold):
            #l'utente è stato correttamente riconosciuto quindi devo inviare tutto a rasa
            toSend = RecognizedSpoke()
            toSend.msg = text_to_send.data
            toSend.id = id_max
            pub1.publish(toSend)
            print('ti riconosco',toSend)

            # natural learning 
            if id_voice_prob_arr[id_max] < 0.28:
                natural_learning_voice.publish(id_max)
               

        else:
            print('non ti  riconosco') #qui bisogna avviare la registrazione
            pub_recogizer_node.publish(Bool(True))
            mario = startVoiceRegistration()
            print('ricevuta risposta'  ,mario)
            #l'utente non è stato correttamente riconosciuto
            # pub2.publish("I can't recognize you")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)

    


def listener():
    rospy.Subscriber('InterpretedText', String, recognize_user)
    rospy.spin()

if __name__ == '__main__':
    listener()