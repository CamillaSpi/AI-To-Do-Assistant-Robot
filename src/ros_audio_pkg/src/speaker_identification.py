#!/usr/bin/python3

"""
This is a Python script that uses the ROS framework and several other libraries, including Tensorflow, NumPy, and pickle, to perform speaker identification. 
The script loads a pre-trained deep learning model (deep_speaker.h5) that has been trained to recognize and compare speaker's voice.

The elaboration function takes audio data as input, processes it, and returns 
the audio data in a format that can be used by the deep learning model. 
The registration function takes input from a microphone and uses the elaboration 
function to process the audio data, and then save the data in the features_dataBase, using phrases that the robot will say to the user to 
guide him through the registration process, asking them to repeat certain phrases to improve the accuracy of the model.

The listener function subscribes to a ROS topic for microphone data, and calls the registration function when new data is received. 
The script also uses the ros_audio_pkg package and srv to publish and receive data from ROS topics.
The script also uses a Lock object to prevent multiple threads from accessing and modifying the shared variables 
at the same time, this can be seen in registration function and listener function.

"""

import rospy
from std_msgs.msg import Int16MultiArray,Float32MultiArray,Int16
import numpy as np
import os

from identification.deep_speaker.audio import get_mfcc
from identification.deep_speaker.model import get_deep_speaker
from identification.utils import batch_cosine_similarity, dist2id
from std_msgs.msg import Int16MultiArray, String
from identification.identities_mng import save_identities, load_identities
from ros_audio_pkg.srv import idLabel,Registration
import rospy
from threading import Lock



REF_PATH = os.path.dirname(os.path.abspath(__file__))
RATE = 16000
lock = Lock()
global prob_voices
global number_of_users
global features_dataBase
global labels
global last_features

# Load model, siamese network based on resnet/vgg. trained with triplet loss. publicly available on keras.
model = get_deep_speaker(os.path.join(REF_PATH,'deep_speaker.h5'))

# Threshold
TH = 0.60

pub1 = rospy.Publisher('toSpeech', String, queue_size=10)

def elaboration(data):
    audio_data = np.array(data)
    audio_data = audio_data.astype(np.float32, order='C') / 32768.0
    ukn = get_mfcc(audio_data, RATE)
    # Prediction
    ukn = model.predict(np.expand_dims(ukn, 0))
    return ukn

# Phrases to repeat during recording
phrases = ["Mi sembra di non conoscerti, dimmi il tuo nome","ora ripeti le seguenti frasi: aggiungi attività corsa nella categoria palestra per domani", "rimuovi la categoria studio in università","aggiorna l'attività passeggiata in personale" , "mostra le mie attività", "ricordami di suonare la chitarra nel tempo libero"]

def registration(msg):
    global features_dataBase
    global labels
    global number_of_users
    lock.acquire()
    for msg in phrases:
        pub1.publish(msg)
        print(msg)
        audioAndData = rospy.wait_for_message("RecivedAudio",Int16MultiArray) 
        data = audioAndData.data
        ukn = elaboration(data)
        try:
            features_dataBase = np.concatenate((features_dataBase,ukn),axis=0)
        except:
            features_dataBase = np.array([ukn[0]])
        labels.append(number_of_users)
    pub1.publish("Perfetto, ti ho riconosciuto")
    rospy.loginfo("Perfetto, ti ho riconosciuto")
    number_of_users+=1
    lock.release()
    return 'ACK'



def listener():
    global prob_voices
    global number_of_users
    global features_dataBase
    global labels
    global last_features
    rospy.init_node('reidentification_node', anonymous=True)
    features_dataBase,labels,number_of_users = load_identities()
    try:
        while not rospy.is_shutdown():
            

            recivedAudio = rospy.wait_for_message("RecivedAudio",Int16MultiArray) 
            lock.acquire()

            last_features = ukn = elaboration(recivedAudio.data)

            if len(features_dataBase) > 0:
                # Distance between the sample and the support set
                emb_voice = np.repeat(ukn, len(features_dataBase), 0)
                # using np.repeat allows us to optimize matrix operations later
                cos_dist = batch_cosine_similarity(np.array(features_dataBase), emb_voice)
                
                _, prob_voices = dist2id(cos_dist, labels, TH, mode='avg') # prob_voices contains the different probabilities divided by the users
                print("voice probability", prob_voices)
            else:
                prob_voices = [] 
            lock.release()

    except rospy.exceptions.ROSInterruptException:
        rospy.loginfo("vado in close speaker")
        save_identities(features_dataBase,labels,number_of_users)
        rospy.loginfo("Salvato db speaker")

def return_idLabel(req):
    global prob_voices
    toReturn = Float32MultiArray() 
    lock.acquire()
    toReturn.data = prob_voices
    lock.release()
    return toReturn

def naturalLearning(msg):
    global last_features
    global features_dataBase
    global labels
    id = msg.data

    lock.acquire()
    print(features_dataBase.shape, len(labels))
    if last_features.all()!=None:
        rospy.loginfo('added new campionbe')
        try:
            features_dataBase = np.concatenate((features_dataBase,last_features),axis=0)
        except:
            features_dataBase = np.array([last_features[0]])
        labels.append(id)
    lock.release()




def voiceLabelServer():
    s = rospy.Service('voiceLabelServices', idLabel, return_idLabel)
    s = rospy.Service('voiceRegistrationService', Registration, registration)
    p = rospy.Subscriber(
        'naturalLearningVoice', Int16, naturalLearning)

    rospy.loginfo("readyToGiveLabels")

if __name__ == '__main__':
    voiceLabelServer()
    listener()