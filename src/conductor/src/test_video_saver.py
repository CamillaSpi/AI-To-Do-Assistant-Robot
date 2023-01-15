#!/usr/bin/python3
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
out = cv2.VideoWriter('/home/mattia/outside_pepper_nando.avi', fourcc, 20.0, size)
    
def listener():
     #qua fare un'array in cui mandiamo entrambe le cose 
    try:
        while not rospy.is_shutdown(): 
            rospy.loginfo('added message')
            img = rospy.wait_for_message("in_rgb1", Image) 
            img = bridge.imgmsg_to_cv2(img)
            img = cv2.resize(img, size)
            out.write(img)
            cv2.imshow("Emotion Demo", img)
            k = cv2.waitKey(5)
    except rospy.exceptions.ROSInterruptException:
        rospy.loginfo("vado in close in massiccianza e salvo il file")
        out.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    listener()