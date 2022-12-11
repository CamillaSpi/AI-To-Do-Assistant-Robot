#!/usr/bin/env python3
import os
import cv2
import rospy
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy
import numpy as np
from vision_msgs.msg import Detection2DArray, ObjectHypothesisWithPose

import json
from json import JSONEncoder
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input

REF_PATH = os.path.dirname(os.path.abspath(__file__))


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def save_identities(path):
    global database
    global labels
    to_save = {'dataset':database, 'labels': labels}
    print("sono in save")
    with open(path + '/json_data.json','w') as out_file:
        json.dump(to_save,out_file,cls=NumpyArrayEncoder)
        

def load_identities(path):
    print("sono in load")
    global database, labels
    try:
        with open(path + '/json_data.json','r') as in_file:
            tmp= json.load(in_file)
        dataset = np.asarray(tmp['dataset'])
        labels = np.asarray(tmp['labels'])
        print("sono in load identities", len(dataset))
        return dataset,labels
    except:
        return [],[]

rospy.init_node('reidentification_face_node')
pub = rospy.Publisher('identity', Detection2DArray, queue_size=2)

# Load the VGG-Face model based on ResNet-50
face_reco_model = VGGFace(model='resnet50', include_top=False, pooling='avg')
padding = 0.2
INPUT_SIZE = (224,224)
global database 
global labels
global actual_id
database,labels = load_identities(REF_PATH)
actual_id = 0
if len(labels):
    actual_id = max(labels) + 1

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
from datetime import datetime

def registration():
    t1 = datetime.now()
    print('non ti conosco... Rimani fermo ')
    for _ in range(10):
        msg = rospy.wait_for_message('face_reidentification',Detection2DArray)
        im = ros_numpy.numpify(msg.detections[0].source_img)
        for d in msg.detections:
            # Preprocess image
            d,resized_face = elaboration(d,im)
            feature_vector = extract_features(face_reco_model, resized_face)
            database.append(feature_vector)
            labels.append(actual_id)
    # Predict
    t2 = datetime.now()
    print('la procedura di registrazione ha impiegato' ,(t2-t1))

def elaboration(d,im):
    bbox_0 = d.bbox.center.y - d.bbox.size_y/2
    bbox_1 = d.bbox.center.x - d.bbox.size_x/2
    bbox_2 = d.bbox.size_x + bbox_0
    bbox_3 = d.bbox.size_y + bbox_1
    padding_px = int(padding*max(d.bbox.size_y,d.bbox.size_x))
    face = im[round(max(0,bbox_1-padding_px)):round(min(bbox_3+padding_px,im.shape[0]-1)),round(max(0,bbox_0-padding_px)):round(min(bbox_2+padding_px, im.shape[1]-1))]
    face = face[ face.shape[0]//2 - face.shape[1]//2 : face.shape[0]//2 + face.shape[1]//2, :, :]
    resized_face = cv2.resize(face,INPUT_SIZE)
    return d,resized_face


def predict_identity(resized_face,rejection_threshold=0.5):
    global actual_id
    if len(database) > 0 :
        feature_vector = extract_features(face_reco_model, resized_face).reshape(-1,2048)
        emb_face = np.repeat(feature_vector, len(database), 0).reshape(-1,2048)
        cos_dist = batch_cosine_similarity(np.array(database), emb_face)
        id_label = dist2id(cos_dist, labels, rejection_threshold, mode='avg')
    else:
        registration()
        id_label = actual_id
    return (id_label)

def face_reidentification(msg):
    im = ros_numpy.numpify(msg.detections[0].source_img)
    for d in msg.detections:
        # Preprocess image
        d,resized_face = elaboration(d,im)
        # Predict
        o = ObjectHypothesisWithPose()
        o.id = predict_identity(resized_face)
        d.results.append(o)
    return msg

   
def recognize():
    try:
        while not rospy.is_shutdown():
            msg = rospy.wait_for_message('face_reidentification',Detection2DArray)
            to_publish = face_reidentification(msg)
            pub.publish(to_publish)

    except rospy.exceptions.ROSInterruptException:
        print("vado in close")
        # save_identities()


if __name__ == '__main__':
    recognize()

