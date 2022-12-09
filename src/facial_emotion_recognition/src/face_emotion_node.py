#!/usr/bin/env python3
import numpy as np
import cv2
import tensorflow as tf
import os
import rospy
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2D, Detection2DArray, ObjectHypothesisWithPose
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy
from threading import Lock


# Initialize emotion classifier
from tensorflow.keras.models import load_model

emotionModel = os.path.join(os.path.dirname(__file__),'emotion.hdf5')
emotionNet = load_model(emotionModel)
emotionList = ['surprise','fear','disgust','happiness','sadness','anger','neutral']
padding = 0.2
MEANS=np.array([131.0912, 103.8827, 91.4953])
INPUT_SIZE = (224,224)


rospy.init_node('face_emotion_node')
pub = rospy.Publisher('emotion', Detection2DArray, queue_size=2)
image_lock = Lock()
image = None

def rcv_boxes(msg):
    global image
    image_lock.acquire()
    if image is None: 
        im = None
    else: 
        im = image.copy()

    image_lock.release()
    if im is None: return
    #frame = ros_numpy.numpify(msg.detections[0].source_img)
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
        blob = np.array([resized_face.astype(float)-MEANS])
        # Predict
        emotionPreds = emotionNet.predict(blob)
        o = ObjectHypothesisWithPose()
        o.id = emotionPreds[0].argmax()
        d.results.append(o)
    pub.publish(msg)

def rcv_image(msg):
    global image
    rospy.loginfo('image here')
    image_lock.acquire()
    image = ros_numpy.numpify(msg)
    image_lock.release()



si = rospy.Subscriber("image", Image, rcv_image)
sd = rospy.Subscriber("detection", Detection2DArray, rcv_boxes)


try:
    rospy.spin()

except KeyboardInterrupt:
    print("Shutting down")