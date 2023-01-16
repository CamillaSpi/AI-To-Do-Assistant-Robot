#!/usr/bin/python3
"""
Used in testing, specifically when the use of pepper was not possible

This script is a simple ROS service that receives a request to load a specific URL on a tablet device. 
The service is defined by the LoadUrl class, which takes a single string argument as the URL to be loaded. 
The service's callback function, handle_speech, simply prints the received URL and returns an acknowledgement string. 
The service is initialized and advertised under the name 'load_url' and the script enters a spin loop to continuously 
listen for incoming requests. When a request is received, the handle_speech function is called and the URL is printed to the console.
"""

from pepper_nodes.srv import LoadUrl
import rospy

def handle_speech(req):
    print("I'm sending to tablet ", req)
    return 'ACK'

def url_server():
    rospy.init_node('url_service')
    s = rospy.Service('load_url', LoadUrl, handle_speech)
    rospy.loginfo("url")
    rospy.spin()

if __name__ == "__main__":
    url_server()

