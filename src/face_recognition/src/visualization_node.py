#!/usr/bin/env python3

"""
This script is a ROS node that subscribes to a topic called "identity" and is expecting messages of type Detection2DArray. 
It uses the cv2 library to display an image with the text "recognized user" or "unrecognized user" depending on the detection 
results in the message. The script also uses the ros_numpy library to convert the sensor_msgs/Image message to a numpy array, 
which is then passed to cv2. It also has a global variable i that is used to save the image to file with a incremented name, 
but the function is commented out. The script also has a try-catch block to handle keyboard interrupts and shut down the node gracefully.

Only images containing at least one face will then be displayed.
"""

import rospy
from vision_msgs.msg import Detection2DArray
import cv2
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy

import os


REF_PATH = os.path.dirname(os.path.abspath(__file__))

rospy.init_node('visualization_node')

global i 
i = 0
def rcv_identity(msg):
    global image
    global i
    frame_face = None
    for d in msg.detections:
        if (frame_face is None):
            frame_face = ros_numpy.numpify(d.source_img)
        id = d.results[0].id
        identity = 'unrecognized user'
        if id >= 0:
            identity = 'recognized user'
        cv2.putText(frame_face, identity, (round(d.bbox.center.y-d.bbox.size_y/2+d.bbox.size_x //20), round(d.bbox.center.x-d.bbox.size_x/2+d.bbox.size_y//20)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("identity Demo", frame_face)
    # cv2.imwrite(REF_PATH + '/../cameraAcquisition/framePepper'+str(i)+'.jpg',frame_face)
    # i+=1
    cv2.waitKey(5)

sd = rospy.Subscriber("identity", Detection2DArray, rcv_identity)

try:
    rospy.spin()

except KeyboardInterrupt:
    rospy.loginfo("Shutting down")