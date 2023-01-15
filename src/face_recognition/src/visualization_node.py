#!/usr/bin/env python3
import rospy
from vision_msgs.msg import Detection2DArray
import cv2
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy

from sensor_msgs.msg import Image
import os


REF_PATH = os.path.dirname(os.path.abspath(__file__))

rospy.init_node('visualization_node')

global i 
i = 0
def rcv_identity(msg):
    global image
    global i
    #rospy.loginfo('detection here')
    frame_face = None
    for d in msg.detections:
        if (frame_face is None):
            frame_face = ros_numpy.numpify(d.source_img)
        id = d.results[0].id
        identity = 'unrecognized user'
        if id >= 0:
            identity = 'recognized user'
        #rospy.loginfo(identity)
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