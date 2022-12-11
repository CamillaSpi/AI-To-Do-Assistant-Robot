#!/usr/bin/env python3
import numpy as np
import cv2
import os
import rospy
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2D, Detection2DArray, ObjectHypothesisWithPose
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy

import json
from json import JSONEncoder

from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
from scipy.spatial.distance import cosine
from datetime import datetime

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def save_identities(dataset,labels, path):
    to_save = {'dataset':dataset,'labels':labels}
    print("sono in save")
    with open(path + '/json_data.json','w') as out_file:
        json.dump(to_save,out_file,cls=NumpyArrayEncoder)

 
def load_identities(path):
    print("sono in load")
    try:
        with open(path + '/json_data.json','r') as in_file:
            tmp= json.load(in_file)
        dataset = np.asarray(tmp['dataset'])
        labels = np.asarray(tmp['labels'])
        print("sono in load identities", len(dataset))
        return dataset,labels
    except:
        return [],[]

rospy.init_node('face_identity_node')
pub = rospy.Publisher('emotion', Detection2DArray, queue_size=2)

# Load the VGG-Face model based on ResNet-50
face_reco_model = VGGFace(model='resnet50', include_top=False, pooling='avg')
padding = 0.2
INPUT_SIZE = (224,224)
X,y = load_identities('/home/nando-child/Scrivania/emotion_det_ws/emotion_det_ws' )



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

def dist2id(distance, y, ths, norm=False, mode='avg', filter_under_th=True):
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
    return ids[np.argmax(ids_prob)]


def extract_features(face_reco_model, filename):
    if type(filename) == 'str':
        faceim = cv2.imread(filename)
    else:
        faceim = filename
    faceim = cv2.resize(faceim, (224,224))
    faceim = preprocess_input([faceim.astype(np.float32)], version=2)
    feature_vector = (face_reco_model.predict(faceim)).flatten()
    return feature_vector


def faceReidentification(frame,rejection_threshold=0.5):
    t7 = datetime.now()
    feature_vector = extract_features(face_reco_model, frame)
    t8 = datetime.now()
    print("Ho fatto la extract feature e ci ho messo", t8-t7)
    #min_distance = [10, 1000000000000]
    print(len(X))
    emb_face = np.repeat(feature_vector, len(X), 0)
    # faccio distanza coseno con tutti quanti gli elementi.
    cos_dist = batch_cosine_similarity(np.array(X), emb_face)
    id_label = dist2id(cos_dist, y, rejection_threshold, mode='avg') #id_label saranno id incrementali
    print(id_label)
    return int(id_label)

def face_reidentification(msg):
    t3 = datetime.now()
    im = ros_numpy.numpify(msg.detections[0].source_img)
    for d in msg.detections:
        bbox_0 = d.bbox.center.y - d.bbox.size_y/2
        bbox_1 = d.bbox.center.x - d.bbox.size_x/2
        bbox_2 = d.bbox.size_x + bbox_0
        bbox_3 = d.bbox.size_y + bbox_1
        padding_px = int(padding*max(d.bbox.size_y,d.bbox.size_x))
        face = im[round(max(0,bbox_1-padding_px)):round(min(bbox_3+padding_px,im.shape[0]-1)),round(max(0,bbox_0-padding_px)):round(min(bbox_2+padding_px, im.shape[1]-1))]
        face = face[ face.shape[0]//2 - face.shape[1]//2 : face.shape[0]//2 + face.shape[1]//2, :, :]
        # Preprocess image
        resized_face = cv2.resize(face,INPUT_SIZE)
        # Predict
        o = ObjectHypothesisWithPose()
        t5 = datetime.now()
        o.id = faceReidentification(resized_face)
        t6 = datetime.now()
        d.results.append(o)
    print('face_reditenficiation')
    t4 = datetime.now()
    print("sono nella reidentification e ci ho messo: ",t4-t3, "la reidentification ci ha messo: ", t6-t5, "e sono le", datetime.now())
    pub.publish(msg)

   

si = rospy.Subscriber("face_reidentification", Detection2DArray, face_reidentification)

try:
    rospy.spin()

except KeyboardInterrupt:
    print("Shutting down")
