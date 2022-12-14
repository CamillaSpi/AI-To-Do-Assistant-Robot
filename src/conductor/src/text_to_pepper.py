#!/usr/bin/python3
import rospy
from std_msgs.msg import String,Bool
import numpy as np
from pepper_nodes.srv import *


# Init node
rospy.init_node('text_to_pepper', anonymous=True)
rospy.wait_for_service('tts')
pub = rospy.Publisher('isListening', Bool)
tts = rospy.ServiceProxy('tts', Text2Speech)
# this is called from the background thread
def callback(msg):
    pub.publish(Bool(False))
    try:
        resp = tts(msg.data).ack
        if resp!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    pub.publish(Bool(True))
    
def listener():
    rospy.Subscriber("toSpeech", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()