#!/usr/bin/env python3


"""

This script is a ROS node that detects faces in an image stream, publishes the bounding
boxes of the detected faces as a Detection2DArray message, and if the --listen_on_detect option is set to True, 
it also publishes a Bool message on the "isListening" topic. The node uses OpenCV's DNN (deep neural network) module 
to detect the faces. The DNN model used is the "opencv_face_detector" and the corresponding prototxt file is "opencv_face_detector.pbtxt". 
The script starts by loading the model and setting up the node, then it defines a detect_face function that is called every time a 
new image message is received, from the topic in_rgb1 to which it is subrscibed. The function first converts the image message to a numpy array and then passes it to the getFaceBox 
function, which applies the DNN model to the image and returns the image with bounding boxes around the detected faces and a list of 
bounding boxes. The script then creates a Detection2DArray message and appends a Detection2D message for each bounding box, and publishes 
the message. 

The --listen_on_detect args it allows us to decide if the microphone should be deactivated in case of non-detect of the person

"""

import cv2
import os
import rospy
from optparse import OptionParser
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from vision_msgs.msg import Detection2D, Detection2DArray
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy



def getFaceBox(net, frame, conf_threshold=0.8):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold and detections[0, 0, i, 5]<1 and detections[0, 0, i, 6]<1:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/300)), 8)
    return frameOpencvDnn, bboxes


DET_PATHproto=os.path.join(os.path.dirname(__file__),'opencv_face_detector.pbtxt')
DET_PATHmodel=os.path.join(os.path.dirname(__file__),'opencv_face_detector_uint8.pb')
# Initialize detector
faceProto = DET_PATHproto
faceModel = DET_PATHmodel

faceNet = cv2.dnn.readNet(faceModel, faceProto)


rospy.init_node('detector_face_node')
pub = rospy.Publisher('face_reidentification', Detection2DArray, queue_size=2)
pub2 = rospy.Publisher('isListening', Bool, queue_size=10)

parser = OptionParser()
parser.add_option("--listen_on_detect", dest="LoD")
(options, args) = parser.parse_args()
listen_on_detect = options.LoD


def detect_face(msg):
    global count
    frame = ros_numpy.numpify(msg)                    # Read frame
    frameFace, bboxes = getFaceBox(faceNet, frame)     # Get face
    message = Detection2DArray()
    for i,bbox in enumerate(bboxes):
        d = Detection2D()
        # Adjust crop
        d.bbox.size_x = bbox[2]-bbox[0]
        d.bbox.size_y = bbox[3]-bbox[1]
        d.bbox.center.x = bbox[1]+d.bbox.size_x/2
        d.bbox.center.y = bbox[0]+d.bbox.size_y/2
        message.detections.append(d)
    if len(message.detections)>0:
        message.detections[0].source_img = ros_numpy.msgify(Image,frameFace,encoding ='rgb8')
        pub.publish(message)
        if listen_on_detect == True: pub2.publish(Bool(True))
    else:
        if listen_on_detect == True: pub2.publish(Bool(False))
        rospy.loginfo('no face found')

si = rospy.Subscriber("in_rgb1", Image, detect_face)

try:
    rospy.spin()

except KeyboardInterrupt:
    rospy.loginfo("Shutting down")
