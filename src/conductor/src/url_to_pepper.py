#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import LoadUrl

# Init node
rospy.init_node('url_to_pepper', anonymous=True)
#rospy.wait_for_service('load_url')
print('mario')
load_url = rospy.ServiceProxy('load_url', LoadUrl)
# this is called from the background thread
def callback(msg):
    try:
        print('arriva')
        resp = load_url(msg.data).ack
        if resp!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    rospy.Subscriber("toShow", String, callback)
    print('toshow')
    rospy.spin()

if __name__ == '__main__':
    listener()