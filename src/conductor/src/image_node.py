#!/usr/bin/python3
import rospy
from sensor_msgs.msg import Image
import numpy as np
from pepper_nodes.srv import *
from ros_audio_pkg.msg import RecognizedSpoke
import cv2

pub = rospy.Publisher('image_analysis', Image, queue_size=10)
# Init node
rospy.init_node('image_node', anonymous=True)

# this is called from the background thread.
def callback(msg):
    try:
        print(' sono callback')
        pub.publish(msg)
        cv2.imshow("Emotion Demo", msg)
        k = cv2.waitKey(5) & 0xFF
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    #qua fare un'array in cui mandiamo entrambe le cose 
    rospy.Subscriber("in_rgb", Image, callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()