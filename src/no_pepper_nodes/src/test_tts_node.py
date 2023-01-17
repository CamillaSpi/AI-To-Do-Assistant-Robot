#!/usr/bin/python3
"""
Used in testing, specifically when the use of pepper was not possible

This script is a ROS service that listens for a service call named "tts" of the Text2Speech service type, 
and when called it will execute the handle_speech function. The handle_speech function takes in a request 
variable "req" which is passed in from the service call, and then it prints the request variable to the console 
and returns the string 'ACK' as the response. The tts_server function is responsible for initializing the ROS node,
creating the service, and starting the service.
"""

from pepper_nodes.srv import Text2Speech
import rospy

def handle_speech(req):
    print('Speech ',req)
    return 'ACK'

def tts_server():
    rospy.init_node('tts_service')
    s = rospy.Service('tts', Text2Speech, handle_speech)
    rospy.loginfo("talk")
    rospy.spin()

if __name__ == "__main__":
    tts_server()

