#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from ros_audio_pkg.srv import idLabel
import time

# Init node
rospy.init_node('test', anonymous=True)
#rospy.wait_for_service('load_url')
load_url = rospy.ServiceProxy('voiceLabelServices', idLabel)
# this is called from the background thread
def callback():
    try:
        resp = load_url().id
        print('label ricevuta', resp)
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    print('aspetto 20 sec e chiedo label voice')
    time.sleep(20)
    callback()
    rospy.spin()

if __name__ == '__main__':
    listener()