#!/usr/bin/python3

"""
This python script is a ROS node that listens to a topic called "toSpeech" and when it receives a message it calls a service called "tts" 
(Text2Speech) to make Pepper robot say the message. It first checks if the service "tts" is running and if it isn't it waits for it to start.
Then it creates a publisher called "isListening" which will publish a boolean value indicating whether Pepper is talking or not. 
When a message is received on the "toSpeech" topic it publish on the topic "isListening" the value False, 
in this way it will notify the audio package to mute the microphone because Pepper is about to speak, 
it calls the "tts" service with the message, waits for the acknowledgment and logs any error if the service call fails, then it publish on the topic "isListening" the value True,
so the microphone can be actived.
It then enters a loop to listen for new messages on the topic "toSpeech". 
"""


import rospy
from std_msgs.msg import String,Bool
import numpy as np
from pepper_nodes.srv import *


# Init node
rospy.init_node('text_to_pepper', anonymous=True)
rospy.wait_for_service('tts')
pub = rospy.Publisher('isListening', Bool,queue_size=10)
tts = rospy.ServiceProxy('tts', Text2Speech)
# this is called from the background thread
def callback(msg):
    pub.publish(Bool(False))
    try:
        resp = tts(msg.data).ack
        if resp!= 'ACK':
            rospy.loginfo("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s", e)
    pub.publish(Bool(True))
    
def listener():
    rospy.Subscriber("toSpeech", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()