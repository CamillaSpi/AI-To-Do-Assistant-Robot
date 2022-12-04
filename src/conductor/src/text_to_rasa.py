#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import *
from ros_audio_pkg.msg import RecognizedSpoke

pub = rospy.Publisher('text2answer', RecognizedSpoke, queue_size=10)
# Init node
rospy.init_node('text_to_rasa', anonymous=True)

# this is called from the background thread
def callback(msg):
    try:
        #resp = tts(msg.data)
        print(msg, ' sono callback')
        pub.publish(msg)
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    #qua fare un'array in cui mandiamo entrambe le cose 
    rospy.Subscriber("recognized_msg", RecognizedSpoke, callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()