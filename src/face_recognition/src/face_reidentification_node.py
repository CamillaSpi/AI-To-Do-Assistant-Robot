#!/usr/bin/env python3

"""


This script is a ROS node that uses the VGGFace library to perform face recognition on a video stream. 
The node is subscribed to the topic face_reidentification on which, in the presence of one or more people, the image and information relating to the 
boundingbox are published. The "cropped" face features are extracted and then the detected face is compared to a database of 
known faces to identify the person. This comparison is made through the two functions batch_cosine_similarity and dist2id, using ad disrance the cosine distance.
The node also includes functionality to save the database to a json file 
and to load the database from a json file. The node publishes the identity of the person along with the detection 
of the face to a topic called "identity". 

This code defines two functions, save_identities() and load_identities(), 
which are used to save and load a dataset and labels from a json file. 
The NumpyArrayEncoder class is used to convert numpy arrays to a format that can be dumped to json.

The save_identities() function uses the json.dump() method to write the dataset, 
labels, and number of users to a json file. The cls parameter is used to specify that 
the NumpyArrayEncoder class should be used to convert the numpy arrays.

The load_identities() function uses the json.load() method to read the json file and 
convert it back to numpy arrays. If the json file cannot be read, the function returns empty arrays.
This script defines a function called "registration" which is used to register new users. 

When the function is called (when a message on topic startRegistration is published), it initializes some global variables, including a variable called "number_of_users" which 
keeps track of the number of registered users. The function then enters a loop which listens for messages on the "face_reidentification" 
topic, which contain images of faces. For each image received, the function performs some image processing to extract features from the face, 
and appends these features to a global variable called "database". The function also appends a label to a global variable called "labels", 
which corresponds to the current value of "number_of_users". When the loop exits, the function increments the "number_of_users" variable, 
releases a lock, and prints the time it took to register the user.

"""



from datetime import datetime
import os
import cv2
import rospy
from scipy import special
import ros_numpy  # pip3 install git+https://github.com/eric-wieser/ros_numpy
import numpy as np
from vision_msgs.msg import Detection2DArray, ObjectHypothesisWithPose

from face_recognition.srv import video_detect_user
from std_msgs.msg import Float32MultiArray, MultiArrayDimension, Bool

import json
from json import JSONEncoder
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input

from threading import Lock

REF_PATH = os.path.dirname(os.path.abspath(__file__))

# Server Initialization
rospy.init_node('reidentification_face_node')
global actualLabels
actualLabels = Float32MultiArray()


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        return JSONEncoder.default(self, obj)


def save_identities():
    global database
    global labels
    global number_of_users
    to_save = {'dataset': database, 'labels': labels,'number_of_users':number_of_users}
    rospy.loginfo("sono in save")
    with open(REF_PATH + '/../dataBase/json_data.json', 'w') as out_file:
        json.dump(to_save, out_file, cls=NumpyArrayEncoder)


def load_identities():
    rospy.loginfo("sono in load")
    try:
        with open(REF_PATH + '/../dataBase/json_data.json', 'r') as in_file:
            tmp = json.load(in_file)
        dataset = np.asarray(tmp['dataset'])
        labels = np.asarray(tmp['labels'],dtype=np.int32)
        number_of_users = tmp['number_of_users']
        return dataset, labels,int(number_of_users)
    except:
        return np.array([]), np.array([]),0


pub = rospy.Publisher('identity', Detection2DArray, queue_size=2)

# Load the VGG-Face model based on ResNet-50
face_reco_model = VGGFace(model='resnet50', include_top=False, pooling='avg')
padding = 0.2
INPUT_SIZE = (224, 224)
global database
global labels
global number_of_users
lock = Lock()
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
            return 0,[0]

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

    ids_prob = np.array(ids_prob)/1000
    ids_prob_soft = special.softmax(ids_prob)

    idmax = ids[np.argmax(ids_prob)]
    if ids_prob_soft[idmax] < 0.75:
        idmax = -1
    return idmax, ids_prob_soft


def extract_features(face_reco_model, filename):
    if type(filename) == 'str':
        faceim = cv2.imread(filename)
    else:
        faceim = filename
    faceim = cv2.resize(faceim, (224, 224))
    faceim = preprocess_input([faceim.astype(np.float32)], version=2)
    feature_vector = (face_reco_model.predict(faceim, verbose=0))
    return feature_vector


def registration(msg):
    global number_of_users
    global database
    global labels
    lock.acquire()
    t1 = datetime.now()
    rospy.loginfo('non ti conosco... Rimani fermo ')
    for x in range(10):
        msg = rospy.wait_for_message('face_reidentification', Detection2DArray)
        im = ros_numpy.numpify(msg.detections[0].source_img)
        for d in msg.detections:
            # Preprocess image
            d, resized_face = elaboration(d, im)
            feature_vector = extract_features(face_reco_model, resized_face)
            if database.size <=0:
                database = feature_vector
            else:
                database = np.concatenate((database, feature_vector))
            labels = np.append(labels,number_of_users)
    number_of_users +=1
    lock.release()
    t2 = datetime.now()
    print('la procedura di registrazione ha impiegato', (t2-t1))


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


def predict_identity(resized_face, rejection_threshold=7000):
    global number_of_users
    if len(database) > 0:
        feature_vector = extract_features(
            face_reco_model, resized_face)
        emb_face = np.repeat(feature_vector, len(
            database), 0)
        cos_dist = batch_cosine_similarity(np.array(database), emb_face)
        id_label, ids_prob = dist2id(
            cos_dist, labels, rejection_threshold, mode='avg',filter_under_th=number_of_users==1)
    else:
        id_label = number_of_users      
        ids_prob = []
    return (id_label), ids_prob


def face_reidentification(msg):
    global actualLabels
    lock.acquire()
    actualLabels = Float32MultiArray()
    im = ros_numpy.numpify(msg.detections[0].source_img)
    for i, d in enumerate(msg.detections):
        # Preprocess image
        d, resized_face = elaboration(d, im)
        # Predict
        o = ObjectHypothesisWithPose()
        o.id, ids_prob = predict_identity(resized_face)
        d.results.append(o)

        for j in range(len(ids_prob)):
            actualLabels.data.append(ids_prob[j])
    lock.release()
    return msg


def recognize():
    s = rospy.Service('videoLabelServices', video_detect_user, handle_service)
    rospy.logdebug('image server READY.')
    rospy.loginfo("vado sotto lo spin")
    try:
        while not rospy.is_shutdown():
            msg = rospy.wait_for_message(
                'face_reidentification', Detection2DArray)
            to_publish = face_reidentification(msg)
            pub.publish(to_publish)
        rospy.loginfo('vado in close Face')
        save_identities()

    except rospy.exceptions.ROSInterruptException or rospy.exceptions.ROSException:
        rospy.loginfo("vado in close Face")
        save_identities()
        rospy.loginfo("Salvato db face")

def handle_service(req):
    global actualLabels
    lock.acquire()

    thing = MultiArrayDimension()
    thing.stride = number_of_users
    try:
        actualLabels.layout.dim.append(thing)
    except NameError:
        rospy.loginfo("in except")
        actualLabels.data = []
    lock.release()
    return actualLabels


if __name__ == '__main__':
    pub_recogizer_node = rospy.Subscriber(
        'startRegistration', Bool, registration)
    recognize()
