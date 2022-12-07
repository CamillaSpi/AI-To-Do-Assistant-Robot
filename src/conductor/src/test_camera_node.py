#!/usr/bin/python3
import rospy
from sensor_msgs.msg import Image
import numpy as np
from pepper_nodes.srv import *
from ros_audio_pkg.msg import RecognizedSpoke
import cv2
import time

pub = rospy.Publisher('in_rgb', Image, queue_size=10)
# Init node
rospy.init_node('test_camera_input', anonymous=True)

    
def listener():    
    cap = cv2.VideoCapture(0)                   # Read frame
    time.sleep(5)
    print('test camera On')
    _, frame = cap.read()
    while not rospy.is_shutdown():
        _, frame = cap.read()
        pub.publish(frame)

if __name__ == '__main__':
    listener()