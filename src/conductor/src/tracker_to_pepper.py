#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import Tracker
import time

# Init node
rospy.init_node('tracker_to_pepper', anonymous=True)
execute_animation = rospy.ServiceProxy('animation_node', Tracker)
# this is called from the background thread
def callback():
    try:
        print('arriva')
        anim = Tracker()
        anim.tracker="face"
        resp = execute_animation(anim).ack
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