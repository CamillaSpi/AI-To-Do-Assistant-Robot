#!/usr/bin/python3

from __future__ import rospy.loginfo_function

from pepper_nodes.srv import Text2Speech
import rospy

def handle_speech(req):
    rospy.loginfo('Speech ',req)
    return 'ACK'

def tts_server():
    rospy.init_node('tts_service')
    s = rospy.Service('tts', Text2Speech, handle_speech)
    rospy.loginfo("talk")
    rospy.spin()

if __name__ == "__main__":
    tts_server()

