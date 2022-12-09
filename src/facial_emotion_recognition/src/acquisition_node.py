#!/usr/bin/env python3
import os
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy
import time

cap = cv2.VideoCapture(0)
time.sleep(0.2)
pub = rospy.Publisher("image_analysis", Image, queue_size=1)
rospy.init_node('acquisition_node', anonymous=True)

def acquire_and_pub():
    while not rospy.is_shutdown():
        _,frame = cap.read()
        time.sleep(0.1) # to send 10fps 
        #ricordati che se hai la telecamera attiva altrove questo non funzionerà
        msg = ros_numpy.msgify(Image,frame,encoding ='rgb8')
        #msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        pub.publish(msg)  
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if rospy.is_shutdown():
            cap.release()

if __name__ == '__main__':
    try:
        acquire_and_pub()
    except rospy.ROSInterruptException:
        pass

            
     
    



