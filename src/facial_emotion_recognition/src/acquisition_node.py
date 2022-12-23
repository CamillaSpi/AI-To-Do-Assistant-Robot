#!/usr/bin/env python3
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

            
     
    



