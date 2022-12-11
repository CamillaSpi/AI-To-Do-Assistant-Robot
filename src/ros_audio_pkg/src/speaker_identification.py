#!/usr/bin/python3
from tensorflow.python.ops.gen_logging_ops import Print
import rospy
from std_msgs.msg import Int16MultiArray
import numpy as np
import pickle
import os

from identification.deep_speaker.audio import get_mfcc
from identification.deep_speaker.model import get_deep_speaker
from identification.utils import batch_cosine_similarity, dist2id
from std_msgs.msg import Int16MultiArray, String
from identification.identities_mng import save_identities, load_identities
from ros_audio_pkg.msg import RecognizedSpoke,AudioAndText
from ros_audio_pkg.srv import idLabel
import rospy



REF_PATH = os.path.dirname(os.path.abspath(__file__))
RATE = 16000
global id_label
# Load model, rete siamese basata su resnet/vgg. addestrata con triplette loss. disponibile pubblicamente su keras, non e la migliore
# la maggior parte implementate in pytorch.
model = get_deep_speaker(os.path.join(REF_PATH,'deep_speaker.h5'))

n_embs = 0
# treshold
TH = 0.60 #0.75 prima

pub1 = rospy.Publisher('toSpeech', String, queue_size=10)
pub2 = rospy.Publisher('recognized_msg', RecognizedSpoke, queue_size=10)

def elaboration(data):
    audio_data = np.array(data)
    # to float32, casto!
    audio_data = audio_data.astype(np.float32, order='C') / 32768.0
    # Processing, prenod lo spettrogramma di MEL(simile all'orecchio umano.)
    ukn = get_mfcc(audio_data, RATE)
    # Prediction
    ukn = model.predict(np.expand_dims(ukn, 0))
    return ukn
# "add activity run in category gym for tomorrow", "add study in university"
phrases = ["I feel like I don't know you, repeat after me: Hi Pepper"]

def registration(id):
    X_new=[]
    y_new=[]
    for msg in phrases:
        pub1.publish(msg)
        print(msg)
        audioAndData = rospy.wait_for_message("AudioAndText",AudioAndText) 
        data = audioAndData.audioData
        ukn = elaboration(data)
        X_new.append(ukn[0])
        y_new.append(id)
    pub1.publish("Stop to repeat with me, let say your name!")
    print("Stop to repeat with me, let say your name!")
    return np.array(X_new),y_new
    



def listener():
    global id_label
    rospy.init_node('reidentification_node', anonymous=True)
    X,y = load_identities(REF_PATH)
    try:
        actual_id = max(y)+1
        print("find some things")
    except:
        print("empty folder ")
        actual_id = 0
    try:
        while not rospy.is_shutdown():
            #mi vado a checkare che si tratti di testo, altrimenti ptrei riconocere il rumore, o comunque avere problemi.
            # co wwait for message, ascolto solo qando voglio, ho operazione "sincrona"
            audioAndData = rospy.wait_for_message("AudioAndText",AudioAndText) 
            data = audioAndData.audioData
            message = audioAndData.spoken_text

            ukn = elaboration(data)

            if len(X) > 0:
                # Distance between the sample and the support set, caolcolo distanza coseno e quelle che ho memorizzato finora.
                emb_voice = np.repeat(ukn, len(X), 0)
                # faccio distanza coseno con tutti quanti gli elementi.
                cos_dist = batch_cosine_similarity(np.array(X), emb_voice)
                
                # Matching, in base alle label e tresh dice distanza.
                # quindi ukn restituisce tutti i valori distanza dei campioni rispetto a ukn. e calcolo la distanza media tra tutti i campioni. 

                id_label = dist2id(cos_dist, y, TH, mode='avg') #id_label saranno id incrementali
            
            if len(X) == 0 or id_label is None:
                #eventuale face recognition
                X_ret,y_ret = registration(actual_id)
                X = np.concatenate((X,X_ret))
                y= y +y_ret
                actual_id+=1
            else:
                print("Ha parlato:", id_label)
                toSend = RecognizedSpoke()
                toSend.msg = message
                toSend.id = id_label
                pub2.publish(toSend)

    except rospy.exceptions.ROSInterruptException:
        print("vado in close")
        # save_identities(X,y,REF_PATH)

def return_idLabel(req):
    global id_label
    print(req)
    return id_label

def voiceLabelServer():
    s = rospy.Service('voiceLabelServices', idLabel, return_idLabel)
    print("readyToGiveLabels")

if __name__ == '__main__':
    voiceLabelServer()
    listener()