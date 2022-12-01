#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np



# Init node
rospy.init_node('text_to_pepper', anonymous=True)


# this is called from the background thread
def callback(msg):
    print("i'm in the callback!")
    try:
        ret = rospy.ServiceProxy('tts',msg.data)
        if ret!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    rospy.Subscriber("toSpeech", String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()