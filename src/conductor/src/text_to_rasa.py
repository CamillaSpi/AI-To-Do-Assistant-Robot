#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import *

pub = rospy.Publisher('text_to_elaborate', String, queue_size=10)
# Init node
rospy.init_node('text_to_rasa', anonymous=True)

# this is called from the background thread
def callback(msg):
    try:
        #resp = tts(msg.data)
        if resp!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    #qua fare un'array in cui mandiamo entrambe le cose 
    rospy.Subscriber("id_user", String, callback)
    rospy.Subscriber("recognized_msg", String, callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()