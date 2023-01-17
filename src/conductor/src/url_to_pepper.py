#!/usr/bin/python3

"""
This python script is a ROS node that listens to a topic called 'toShow' and when a message is received, 
it checks the content of the message and takes appropriate action. If the message contains the string "js", 
it calls the 'execute_js' service by notifying to the related service on Pepper to execute a JavaScript injection on the loaded webpage.
If the message contains the string "reload", it calls the 'execute_js' service by notifying to the related service on Pepper 
to reload the current webpage on the tablet. If the message does not contain "js" or "reload", it calls the 'load_url' service to 
load the URL specified in the message on the tablet. If the service call returns an 'ACK' response, it considers the operation successful, 
otherwise it logs an error message. It also has a publisher 'isListening' that publish a message indicating if the node is currently
executing a command or not.
"""

import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import LoadUrl, ExecuteJS
import time

# Init node
rospy.init_node('url_to_pepper', anonymous=True)
#rospy.wait_for_service('load_url')
load_url = rospy.ServiceProxy('load_url', LoadUrl)
execute_js = rospy.ServiceProxy('execute_js', ExecuteJS)
# this is called from the background thread
def callback(msg):
    try:
        resp = None
        if "js" in msg.data:
            rospy.loginfo("Injected JS")
            script = """var inject = document.getElementById("clickMe");
    inject.click();"""
            resp = execute_js(script).ack
        if 'reload' in msg.data:
            rospy.loginfo("Injected Reload")
            script = """var reload = document.getElementById("refresh");
    reload.click();"""
            resp = execute_js(script).ack
        elif 'js' not in msg.data and 'reload' not in msg.data:
            rospy.loginfo('Send URL')
            resp = load_url(msg.data).ack

        if resp!= 'ACK':
            rospy.loginfo("There is an error in msg, maybe")
            
    except rospy.ServiceException as e:
        rospy.loginfo("Service call failed: %s", e)
    
def listener():
    rospy.Subscriber("toShow", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()