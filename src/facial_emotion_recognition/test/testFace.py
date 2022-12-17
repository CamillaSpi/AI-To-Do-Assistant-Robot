# In case of ModuleNotFoundError: No module named 'keras.engine.topology'
# Change from keras.engine.topology import get_source_inputs 
# to from keras.utils.layer_utils import get_source_inputs
# in file keras_vggface/models.py

import cv2
import numpy as np
import os

from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from scipy import special
import json


REF_PATH = os.path.dirname(os.path.abspath(__file__))

def load_identities():
    print("sono in load")
    try:
        with open(REF_PATH + '/../dataBase/json_data.json', 'r') as in_file:
            tmp = json.load(in_file)
        dataset = np.asarray(tmp['dataset'])
        labels = np.asarray(tmp['labels'])
        number_of_users = tmp['number_of_users']
        return dataset, labels,number_of_users
    except:
        return [], [],0

# This method takes as input the face recognition model and the filename of the image and returns
# the feature vector
def extract_features(face_reco_model, filename):
    faceim = cv2.imread(filename)
    faceim = cv2.resize(faceim, (224,224))
    faceim = preprocess_input([faceim.astype(np.float32)], version=2)
    feature_vector = (face_reco_model.predict(faceim)).flatten()
    return feature_vector

# Load the VGG-Face model based on ResNet-50
face_reco_model = VGGFace(model='resnet50', include_top=False, pooling='avg')

padding = 0.2
INPUT_SIZE = (224, 224)
global database
global labels
global number_of_users
database, labels,number_of_users = load_identities()


def batch_cosine_similarity(x1, x2):
    '''
        x1,x2 must be l2 normalized
    '''

    # https://en.wikipedia.org/wiki/Cosine_similarity
    # 1 = equal direction ; -1 = opposite direction
    mul = np.multiply(x1, x2)
    s = np.sum(mul, axis=1)

    # l1 = np.sum(np.multiply(x1, x1),axis=1)
    # l2 = np.sum(np.multiply(x2, x2), axis=1)
    # as values have have length 1, we don't need to divide by norm (as it is 1)
    return s


def dist2id(distance, y, ths, norm=False, mode='avg', filter_under_th=False):
    d = distance.copy()
    ths = np.array([ths]*len(y))
    y = np.array(y)

    # remove elements under the threshold
    if filter_under_th:
        idx = d >= ths
        d = d[idx]
        y = y[idx]
        ths = ths[idx]

        if d.shape[0] == 0:
            return None

    if norm:
        # norm in case of different thresholds
        d = (d - ths)/(1-ths)

    ids = list(set(y.tolist()))

    ids_prob = []
    for i in ids:
        if mode == 'max':
            ids_prob.append(np.max(d[y == i]))
        if mode == 'avg':
            ids_prob.append(np.mean(d[y == i]))
        if mode == 'min':
            ids_prob.append(np.min(d[y == i]))

    ids_prob = np.array(ids_prob)
    ids_prob_soft = special.softmax(ids_prob)
    return ids[np.argmax(ids_prob)], ids_prob_soft


def extract_features(face_reco_model, filename):
    if type(filename) == 'str':
        faceim = cv2.imread(filename)
    else:
        faceim = filename
    faceim = cv2.resize(faceim, (224, 224))
    faceim = preprocess_input([faceim.astype(np.float32)], version=2)
    feature_vector = (face_reco_model.predict(faceim, verbose=0)).flatten()
    return feature_vector



def elaboration(d, im):
    bbox_0 = d.bbox.center.y - d.bbox.size_y/2
    bbox_1 = d.bbox.center.x - d.bbox.size_x/2
    bbox_2 = d.bbox.size_x + bbox_0
    bbox_3 = d.bbox.size_y + bbox_1
    padding_px = int(padding*max(d.bbox.size_y, d.bbox.size_x))
    face = im[round(max(0, bbox_1-padding_px)):round(min(bbox_3+padding_px, im.shape[0]-1)),
              round(max(0, bbox_0-padding_px)):round(min(bbox_2+padding_px, im.shape[1]-1))]
    face = face[face.shape[0]//2 - face.shape[1] //
                2: face.shape[0]//2 + face.shape[1]//2, :, :]
    resized_face = cv2.resize(face, INPUT_SIZE)
    return d, resized_face


def predict_identity(resized_face, rejection_threshold=0.5):
    global number_of_users
    if len(database) > 0:
        feature_vector = extract_features(
            face_reco_model, resized_face).reshape(-1, 2048)
        emb_face = np.repeat(feature_vector, len(
            database), 0).reshape(-1, 2048)
        cos_dist = batch_cosine_similarity(np.array(database), emb_face)
        # id_label = dist2id(cos_dist, labels, rejection_threshold, mode='avg')
        id_label, ids_prob = dist2id(
            cos_dist, labels, rejection_threshold, mode='avg')
    else:
        id_label = number_of_users        # non so a che serve, probabilmente la togliamo proprio
        ids_prob = []
    return (id_label), ids_prob


def face_reidentification(image):
    global actualLabels
    actualLabels =[]
    id, ids_prob = predict_identity(image)
    print(id, ids_prob)


face_reidentification('/home/nando/Scrivania/DefinitivoCog/src/facial_emotion_recognition/test/0/1.png')