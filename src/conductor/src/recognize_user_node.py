#!/usr/bin/python3
import rospy
from std_msgs.msg import String,Bool,Int16
import numpy as np
from ros_audio_pkg.msg import RecognizedSpoke
from pepper_nodes.srv import *
from ros_audio_pkg.srv import idLabel,Registration
from face_recognition.srv import video_detect_user


#Creating a publisher on text2answer topic on which we will send the messages to rasa
pub1 = rospy.Publisher('text2answer', RecognizedSpoke, queue_size=1)

#Creating a publisher on startRegistration topic on which we will sent a boolean to start the audio registration, when the user is not recognized
pub_recogizer_node = rospy.Publisher('startRegistration', Bool, queue_size=1)

#Creating a publisher on naturalLearningVoice topic on which we will send the information for the natural learning procedure of speech recognition
natural_learning_voice = rospy.Publisher('naturalLearningVoice', Int16, queue_size=10)

rospy.init_node('recognize_user', anonymous=True)
rejection_threshold = 0.55 #threshold value that marks wheter a person is considered recognized or not

#Obtaining datas of identification with voice and video services from speaker identification and face reidentification
rospy.wait_for_service('voiceLabelServices')
rospy.wait_for_service('videoLabelServices')
rospy.wait_for_service('voiceRegistrationService')
obtain_audio_prob = rospy.ServiceProxy('voiceLabelServices', idLabel)
obtain_video_prob = rospy.ServiceProxy('videoLabelServices', video_detect_user)
#audio registration service used when a person is not recognized
startVoiceRegistration = rospy.ServiceProxy('voiceRegistrationService', Registration)



"""
Function to recognize user with both audio and video; we give more importance to the face information, so the probabilities are multiplied 
by a factor that is higher for face probabilities. We use also a threshold value that has to be reached by the sum of the probabilities
between audio and video by every user, if it is not reached the registration of a new, unknown, user starts, publishing on the StartRegistration topic,
and through voiceRegistrationService. 
When the user is recognized we send the information of the id of the user and the text he has told to rasa, publishing on text2answer topic. 
"""
def recognize_user(text_to_send):
    try:

        id_face_prob = obtain_video_prob().answer
        faces_stride = id_face_prob.layout.dim[0].stride
        id_face_prob_arr = np.asarray(id_face_prob.data)
        print("values faces: ", id_face_prob_arr )

        id_voice_prob = obtain_audio_prob().prob_voices
        id_voice_prob_arr = np.asarray(id_voice_prob.data)
        print("value voices", id_voice_prob_arr)
        
        
        start = 0
        max = 0
        id_max = -1
        
        while start != len(id_face_prob_arr):
            stop = start + faces_stride
            sum = np.sum([id_voice_prob_arr*0.40,id_face_prob_arr[start:stop]*0.60], axis = 0)
            if(max < np.max(sum)):
                max = np.max(sum)
                id_max = np.argmax(sum)
            start = stop
        print("id_max",id_max,"max", max)
        if(max>rejection_threshold):
            #user correctly recognized, so RecognizedSpoke that is a structured type composed by the text to analyze and the user id, is sent to rasa
            toSend = RecognizedSpoke()
            toSend.msg = text_to_send.data
            toSend.id = id_max
            pub1.publish(toSend)
            rospy.loginfo('Utente riconosciuto')
            print(str(text_to_send.data))

            #if confidence voice prediction is under a certain threshold it's necessary to start natural learning procedure
            if id_voice_prob_arr[id_max] < 0.35:
                natural_learning_voice.publish(id_max)
        else:
            rospy.loginfo('Utente Non riconosciuto, inizio registrazione') ##user not recognized, it is necessary to start registration
            pub_recogizer_node.publish(Bool(True))
            reg_response = startVoiceRegistration()
            print('ricevuta risposta'  ,reg_response)
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s", e)

    


def listener():
    rospy.Subscriber('InterpretedText', String, recognize_user)
    rospy.spin()

if __name__ == '__main__':
    listener()