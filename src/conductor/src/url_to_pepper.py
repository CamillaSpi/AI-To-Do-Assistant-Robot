#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import *


# Init node
rospy.init_node('url_to_pepper', anonymous=True)
# rospy.wait_for_service('load_url')
# load_url = rospy.ServiceProxy('load_url', LoadUrl)
# this is called from the background thread
def callback(msg):
    print('Send url to pepper ' + msg.data)
    try:
        # resp = load_url(msg.data)
        resp = 'ACK'
        if resp!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    rospy.Subscriber("toShow", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()