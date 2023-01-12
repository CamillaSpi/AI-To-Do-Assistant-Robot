#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy
import os

#da verificare per bene i parametri ottimali
rospy.init_node('acquire_and_save_node', anonymous=True)


REF_PATH = os.path.dirname(os.path.abspath(__file__))

global i 
i=0
def acquire_and_save(msg):
    global i
    print('received img')
    frame = ros_numpy.numpify(msg)  
    cv2.imwrite(REF_PATH + '/../cameraAcquisition/framePepper'+str(i)+'.jpg',frame)
    print('scrivo ' , i)
    i+=1


si = rospy.Subscriber("in_rgb1", Image, acquire_and_save)
print('ciao')
rospy.spin()


            
     
    



