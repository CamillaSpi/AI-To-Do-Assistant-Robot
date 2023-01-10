#!/usr/bin/python3
import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
import time

from cv_bridge import CvBridge
pub = rospy.Publisher('test_images_topic', Image, queue_size=10)
# Init node
rospy.init_node('test_camera_input', anonymous=True)
bridge = CvBridge()
    
def listener():    
    cap = cv2.VideoCapture(0)                   # Read frame
    time.sleep(5)
    print('test camera On')
    _, frame = cap.read()
    while not rospy.is_shutdown():
        _, frame = cap.read()
        frame = bridge.cv2_to_imgmsg(frame)
        pub.publish(frame)

if __name__ == '__main__':
    listener()