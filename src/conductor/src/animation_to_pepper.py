#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import LoadUrl
import time

# Init node
rospy.init_node('animation_to_pepper', anonymous=True)
load_url = rospy.ServiceProxy('animation_node', LoadUrl)
# this is called from the background thread
def callback():
    try:
        print('arriva')
        resp = load_url("animations/Stand/Gestures/Hey_1").ack
        if resp!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    time.sleep(5)
    callback()
    rospy.spin()

if __name__ == '__main__':
    listener()