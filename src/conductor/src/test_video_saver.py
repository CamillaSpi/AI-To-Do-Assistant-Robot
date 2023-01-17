#!/usr/bin/python3

"""
The purpose of this node is to store the video stream captured by pepper.

This script is a ROS node that listens to a topic called "in_rgb1" and subscribes to it. 
The topic is expected to contain images in the form of sensor_msgs/Image messages. 
The script uses cv_bridge library to convert the ROS Image message to a cv2 image. 
Then the script resizes the image to a width of 640 and height of 480. 
The script uses OpenCV's VideoWriter class to create a video file called "outside_pepper.avi" 
and writes the resized image to it. The video's codec is set to XVID and the frames per second is set to 20. 
Then it shows the image on a window called "PepperAcquisition". It waits for 5 milliseconds for a key press and if 
the 'q' key is pressed it quits. If the ROS node is interrupted the script will release the video and close all the windows.

"""

import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge

# Init node
rospy.init_node('image_node', anonymous=True)
bridge = CvBridge()

#getted from pepper
width = 640
height =480
size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('/home/mattia/outside_pepper.avi', fourcc, 20.0, size)
    
def listener():
    try:
        while not rospy.is_shutdown(): 
            rospy.loginfo('added message')
            img = rospy.wait_for_message("in_rgb1", Image) 
            img = bridge.imgmsg_to_cv2(img)
            img = cv2.resize(img, size)
            out.write(img)
            cv2.imshow("PepperAcquisition", img)
            k = cv2.waitKey(5)
    except rospy.exceptions.ROSInterruptException:
        rospy.loginfo("vado in close in massiccianza e salvo il file")
        out.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    listener()