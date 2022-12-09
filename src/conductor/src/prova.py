#!/usr/bin/python3
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
import numpy as np
import cv2
from cv_bridge import CvBridge
 
pub = rospy.Publisher('toShow', String, queue_size=10)
# Init node
rospy.init_node('image_node', anonymous=True)
 
def listener():
 #qua fare un'array in cui mandiamo entrambe le cose 
    try:
        print('ore')
        pub.publish('http://10.0.1.227:80/webPage')
        print('ore')
    except rospy.exceptions.ROSInterruptException:
        print("vado in close in massiccianza")
 
 
if __name__ == '__main__':
 listener()