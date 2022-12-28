#!/usr/bin/python3
from tensorflow.python.ops.gen_logging_ops import Print
import rospy
from std_msgs.msg import Int16MultiArray,Float32MultiArray,Int16
import numpy as np
import pickle
import os

from identification.deep_speaker.audio import get_mfcc
from identification.deep_speaker.model import get_deep_speaker
from identification.utils import batch_cosine_similarity, dist2id
from std_msgs.msg import Int16MultiArray, String,Bool
from identification.identities_mng import save_identities, load_identities
from ros_audio_pkg.msg import RecognizedSpoke,AudioAndText
from ros_audio_pkg.srv import idLabel,Registration
import rospy
from threading import Lock



REF_PATH = os.path.dirname(os.path.abspath(__file__))
RATE = 16000
lock = Lock()
global id_label
global prob_voices
global number_of_users
global features_dataBase
global labels
global last_features

# Load model, rete siamese basata su resnet/vgg. addestrata con triplette loss. disponibile pubblicamente su keras, non e la migliore
# la maggior parte implementate in pytorch.
model = get_deep_speaker(os.path.join(REF_PATH,'deep_speaker.h5'))

n_embs = 0
# treshold
TH = 0.60 #0.75 prima

pub1 = rospy.Publisher('toSpeech', String, queue_size=10)

def elaboration(data):
    audio_data = np.array(data)
    # to float32, casto!
    audio_data = audio_data.astype(np.float32, order='C') / 32768.0
    # Processing, prenod lo spettrogramma di MEL(simile all'orecchio umano.)
    ukn = get_mfcc(audio_data, RATE)
    # Prediction
    ukn = model.predict(np.expand_dims(ukn, 0))
    return ukn
# ,"add activity run in category gym for tomorrow","add activity run in category gym for tomorrow", "remove the category study in university","update the activity walk in personal" , "show my activity", "remind me to play guitar in freetime"
phrases = ["Mi sembra di non conoscerti, ripeti dopo di me: Ciao Pepper","aggiungi attività corsa nella categoria palestra per domani", "rimuovi la categoria studio in università","aggiorna l'attività passeggiata in personale" , "mostra le mie attività", "ricordami di suonare la chitarra nel tempo libero"]

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
    pub1.publish("Perfetto, ti ho riconosciuto, ora dimmi il tuo nome!")
    print("Perfetto, ti ho riconosciuto, ora dimmi il tuo nome!")
    number_of_users+=1
    lock.release()
    return 'ACK'



def listener():
    global id_label
    global prob_voices
    global number_of_users
    global features_dataBase
    global labels
    global last_features
    rospy.init_node('reidentification_node', anonymous=True)
    features_dataBase,labels,number_of_users = load_identities()
    try:
        while not rospy.is_shutdown():
            #mi vado a checkare che si tratti di testo, altrimenti ptrei riconocere il rumore, o comunque avere problemi.
            # co wwait for message, ascolto solo qando voglio, ho operazione "sincrona"
            recivedAudio = rospy.wait_for_message("RecivedAudio",Int16MultiArray) 
            lock.acquire()

            last_features = ukn = elaboration(recivedAudio.data)

            if len(features_dataBase) > 0:
                # Distance between the sample and the support set, caolcolo distanza coseno e quelle che ho memorizzato finora.
                emb_voice = np.repeat(ukn, len(features_dataBase), 0)
                # faccio distanza coseno con tutti quanti gli elementi.
                cos_dist = batch_cosine_similarity(np.array(features_dataBase), emb_voice)
                
                # Matching, in base alle label e tresh dice distanza.
                # quindi ukn restituisce tutti i valori distanza dei campioni rispetto a ukn. e calcolo la distanza media tra tutti i campioni. 

                id_label, prob_voices = dist2id(cos_dist, labels, TH, mode='avg') #id_label saranno id incrementali
                print("prob_voices", prob_voices)
            else:
                prob_voices = [] 
            lock.release()

    except rospy.exceptions.ROSInterruptException:
        print("vado in close")
        save_identities(features_dataBase,labels,number_of_users)

def return_idLabel(req):
    global id_label
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
    # should never be None, but to be safe
    if last_features.all()!=None:
        print('added new campionbe')
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

    print("readyToGiveLabels")

if __name__ == '__main__':
    voiceLabelServer()
    listener()