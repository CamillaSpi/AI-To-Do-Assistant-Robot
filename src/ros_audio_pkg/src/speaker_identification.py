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


REF_PATH = os.path.dirname(os.path.abspath(__file__))
RATE = 16000

# Load model, rete siamese basata su resnet/vgg. addestrata con triplette loss. disponibile pubblicamente su keras, non e la migliore
# la maggior parte implementate in pytorch.
model = get_deep_speaker(os.path.join(REF_PATH,'deep_speaker.h5'))

n_embs = 0
X = []
y = []
# treshold
TH = 0.75


def listener():
    rospy.init_node('reidentification_node', anonymous=True)

    while not rospy.is_shutdown():
        #mi vado a checkare che si tratti di testo, altrimenti ptrei riconocere il rumore, o comunque avere problemi.
        # co wwait for message, ascolto solo qando voglio, ho operazione "sincrona"
        data = rospy.wait_for_message("voice_data",Int16MultiArray) 

        audio_data = np.array(data.data)

        # to float32, casto!
        audio_data = audio_data.astype(np.float32, order='C') / 32768.0

        # Processing, prenod lo spettrogramma di MEL(simile all'orecchio umano.)
        ukn = get_mfcc(audio_data, RATE)

        # Prediction
        ukn = model.predict(np.expand_dims(ukn, 0))

        if len(X) > 0:
            # Distance between the sample and the support set, caolcolo distanza coseno e quelle che ho memorizzato finora.
            emb_voice = np.repeat(ukn, len(X), 0)
            # faccio distanza coseno con tutti quanti gli elementi.
            cos_dist = batch_cosine_similarity(np.array(X), emb_voice)
            
            # Matching, in base alle label e tresh dice distanza.
            # quindi ukn restituisce tutti i valori distanza dei campioni rispetto a ukn. e calcolo la distanza media tra tutti i campioni. 
            id_label = dist2id(cos_dist, y, TH, mode='avg')
        
        if len(X) == 0 or id_label is None:
            c = input("Voce non conosciuta. Vuoi inserire un nuovo campione? (S/N):")
            if c.lower() == 's':
                name = input("Inserisci il nome dello speaker:").lower()
                X.append(ukn[0])
                y.append(name)
        else:
            print("Ha parlato:", id_label)
        
if __name__ == '__main__':
    listener()