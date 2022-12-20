#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import Animation
import time

# Init node
rospy.init_node('animation_to_pepper', anonymous=True)
execute_animation = rospy.ServiceProxy('animation_node', Animation)
# this is called from the background thread
def callback(msg):
    try:
        resp = execute_animation(msg.data).ack
        if resp!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    rospy.Subscriber("animation2Pepper", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()