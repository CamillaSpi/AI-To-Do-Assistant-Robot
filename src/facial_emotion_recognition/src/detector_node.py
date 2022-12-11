#!/usr/bin/env python3
import cv2
import os
import rospy
from sensor_msgs.msg import Image
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
padding = 0.2
count = 10

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
    else:
        print('no face found')

si = rospy.Subscriber("image", Image, detect_face)

try:
    rospy.spin()

except KeyboardInterrupt:
    print("Shutting down")
