#!/usr/bin/python3
import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
from cv_bridge import CvBridge

pub = rospy.Publisher('image_analysis', Image, queue_size=10)
# Init node
rospy.init_node('image_node', anonymous=True)
bridge = CvBridge()
# this is called from the background thread.
def callback(msg):
    try:
        # pub.publish(msg)
        msg = bridge.imgmsg_to_cv2(msg)
        cv2.imshow("Emotion Demo", msg)
        k = cv2.waitKey(5)
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    #qua fare un'array in cui mandiamo entrambe le cose 
    try:
        rospy.Subscriber("in_rgb", Image, callback)
        rospy.spin()
    except rospy.exceptions.ROSInterruptException:
        print("vado in close in massiccianza")
    

if __name__ == '__main__':
    listener()