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
from ros_audio_pkg.msg import RecognizedSpoke

REF_PATH = os.path.dirname(os.path.abspath(__file__))
RATE = 16000

# Load model, rete siamese basata su resnet/vgg. addestrata con triplette loss. disponibile pubblicamente su keras, non e la migliore
# la maggior parte implementate in pytorch.
model = get_deep_speaker(os.path.join(REF_PATH,'deep_speaker.h5'))

n_embs = 0
# treshold
TH = 0.60 #0.75 prima

pub1 = rospy.Publisher('toSpeech', String, queue_size=10)
pub2 = rospy.Publisher('recognized_msg', RecognizedSpoke, queue_size=10)

def elaboration(data):
    
    audio_data = np.array(data.data)
    # to float32, casto!
    audio_data = audio_data.astype(np.float32, order='C') / 32768.0
    # Processing, prenod lo spettrogramma di MEL(simile all'orecchio umano.)
    ukn = get_mfcc(audio_data, RATE)
    # Prediction
    ukn = model.predict(np.expand_dims(ukn, 0))
    return ukn

phrases = ["I feel like I don't know you, repeat after me: Hi Pepper", "add activity run in category gym for tomorrow", "add study in university"]

def registration(id):
    X_new=[]
    y_new=[]
    for msg in phrases:
        pub1.publish(msg)
        print(msg)
        data = rospy.wait_for_message("voice_data",Int16MultiArray) 
        ukn = elaboration(data)
        X_new.append(ukn[0])
        y_new.append(id)
    pub1.publish("Stop to repeat with me, let say your name!")
    print("Stop to repeat with me, let say your name!")
    return X_new,y_new
    



def listener():
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
            data = rospy.wait_for_message("voice_data",Int16MultiArray) 
            message = rospy.wait_for_message("spoken_text",String)

            ukn = elaboration(data)

            if len(X) > 0:
                # Distance between the sample and the support set, caolcolo distanza coseno e quelle che ho memorizzato finora.
                emb_voice = np.repeat(ukn, len(X), 0)
                print("len emb voice: ", len(emb_voice))
                # faccio distanza coseno con tutti quanti gli elementi.
                cos_dist = batch_cosine_similarity(np.array(X), emb_voice)
                
                # Matching, in base alle label e tresh dice distanza.
                # quindi ukn restituisce tutti i valori distanza dei campioni rispetto a ukn. e calcolo la distanza media tra tutti i campioni. 
                print("feature: ", y)
                id_label = dist2id(cos_dist, y, TH, mode='avg') #id_label saranno id incrementali
            
            if len(X) == 0 or id_label is None:
                #eventuale face recognition
                X_ret,y_ret = registration(actual_id)
                X = X + X_ret
                y= y +y_ret
                actual_id+=1
            else:
                print("Ha parlato:", id_label)
                pub2.publish(message)

    except rospy.exceptions.ROSInterruptException:
        print("vado in close")
        save_identities(X,y,REF_PATH)
        
if __name__ == '__main__':
    listener()