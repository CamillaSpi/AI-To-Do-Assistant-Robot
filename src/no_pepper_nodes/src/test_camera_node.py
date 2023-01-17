#!/usr/bin/env python3

"""
Used in testing, specifically when the use of pepper was not possible

This script is a simple implementation of a ROS node that captures video frames from the default camera 
device and publishes them as ROS Image messages on the topic "in_rgb1". 
The node uses the OpenCV library to capture the video frames and the ros_numpy library to convert the frames to ROS Image messages. 
It also uses time.sleep function to set a delay in between frames. The node initializes with a publisher named "in_rgb1" and a sleep 
time of 2 seconds before starting the capturing process. It runs in a while loop until rospy shutdown is called and in each iteration, 
it captures a frame, converts it to ROS Image message, publishes it and sleeps for 0.35 seconds. If the capturing process fails or rospy 
shutdown is called, the function releases the camera.
"""


import rospy
import cv2
from sensor_msgs.msg import Image
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy
import time

cap = cv2.VideoCapture(0)

# Read until video is completed
time.sleep(2)

#da verificare per bene i parametri ottimali
pub = rospy.Publisher("in_rgb1", Image, queue_size=5)
rospy.init_node('acquisition_node', anonymous=True)

def acquire_and_pub():
    while not rospy.is_shutdown():
        time.sleep(0.35)
        ret,frame = cap.read()
        if ret == True:
            msg = ros_numpy.msgify(Image,frame,encoding ='rgb8')
            pub.publish(msg) 
        else:
            if rospy.is_shutdown():
                cap.release()

if __name__ == '__main__':
    try:
        acquire_and_pub()
    except rospy.ROSInterruptException:
        pass
