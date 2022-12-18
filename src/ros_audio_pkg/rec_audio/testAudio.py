import rospy
from std_msgs.msg import Int16MultiArray
import numpy as np
import os
import librosa# importing module
import sys
 
# appending a path
REF_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(REF_PATH + "/../src/")
from identification.deep_speaker.audio import get_mfcc
from identification.deep_speaker.model import get_deep_speaker
from identification.utils import batch_cosine_similarity, dist2id
from identification.identities_mng import load_identities
from glob import glob
from tqdm import tqdm

CHANNELS = 1
RATE = 16000
WIN_SIZE_SEC = 0.03
CHUNK = int(WIN_SIZE_SEC * RATE)
from scipy.io import wavfile
print(os.path.abspath(os.getcwd()))


REF_PATH = os.path.dirname(os.path.abspath(__file__))
RATE = 16000
global id_label
global prob_voices
global number_of_users
global features_dataBase
global labels
global last_features


features_dataBase,labels,number_of_users = load_identities()

# Load model, rete siamese basata su resnet/vgg. addestrata con triplette loss. disponibile pubblicamente su keras, non e la migliore
# la maggior parte implementate in pytorch.
model = get_deep_speaker(REF_PATH+'/../src/deep_speaker.h5')

n_embs = 0
# treshold
TH = 0.60 #0.75 prima


def elaboration(data):
    audio_data = np.array(data)
    # to float32, casto!
    audio_data = audio_data.astype(np.float32, order='C') / 32768.0
    # Processing, prenod lo spettrogramma di MEL(simile all'orecchio umano.)
    ukn = get_mfcc(audio_data, RATE)
    # Prediction
    ukn = model.predict(np.expand_dims(ukn, 0))
    return ukn


def listener(data):
    ukn = elaboration(data)
    if len(features_dataBase) > 0:
            # Distance between the sample and the support set, caolcolo distanza coseno e quelle che ho memorizzato finora.
        emb_voice = np.repeat(ukn, len(features_dataBase), 0)
        # faccio distanza coseno con tutti quanti gli elementi.
        cos_dist = batch_cosine_similarity(np.array(features_dataBase), emb_voice)
        
        # Matching, in base alle label e tresh dice distanza.
        # quindi ukn restituisce tutti i valori distanza dei campioni rispetto a ukn. e calcolo la distanza media tra tutti i campioni. 

        id_label, prob_voices = dist2id(cos_dist, labels, TH, mode='avg') #id_label saranno id incrementali
        # print("prob_voices", prob_voices)
        return id_label
    else:
        print('no Db')

number_of_known_people=4
accuracy = 0
count = 0

for i in range(0,number_of_known_people):
    person_path = os.path.join(REF_PATH, str(i).zfill(1))
    person = []
    print(person_path)
    for filename in tqdm(glob(os.path.join(person_path,'*'))):
        if filename == '.DS_Store':
            os.remove(filename)
            continue
        count +=1
        data, x = librosa.load(filename)
        data = int16 = (data * 32767).astype(np.int16)
        if (0 == listener(data)):
            accuracy +=1

print("the accuracy is {:.2f}".format(accuracy/count))