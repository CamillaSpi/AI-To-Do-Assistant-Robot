#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np

'''
This class implements a ROS node that read the video stream published on the specific topic and shows it in a openCV window
'''
class Nodo(object):
    def __init__(self):
        # Params
        self.br = CvBridge()
    
    '''
    This method receives a Image message and converts it to numpy array, then show the image opening a window
    '''
    def callback(self, msg):
        image = self.br.imgmsg_to_cv2(msg)
        cv2.imshow("Pepper Camera", image)
        cv2.waitKey(50)
    
    '''
    THis method subscribes the node to specific topic and starts the node loop
    '''
    def start(self):
        # Subscriber
        rospy.Subscriber("/in_rgb", Image, self.callback)

        rospy.spin()


if __name__ == '__main__':
    rospy.init_node("camera_show_node", anonymous=True)
    my_node = Nodo()
    my_node.start()
