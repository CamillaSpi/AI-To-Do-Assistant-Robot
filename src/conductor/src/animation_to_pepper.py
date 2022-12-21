#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
from pepper_nodes.srv import Animation
import time
import random

# Init node
rospy.init_node('animation_to_pepper', anonymous=True)
execute_animation = rospy.ServiceProxy('animation_node', Animation)
# this is called from the background thread

available_bodyTalk  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def callback(msg):
    if "hai effettuato l'accesso!" in msg.data:
        anim="animations/Stand/Gestures/Hey_4"
    elif "Mi dispiace, non posso aiutarti, puoi ripetere?." in msg.data:
        anim="animations/Stand/Gestures/IDontKnow_1"
    elif "ecco a te" in msg.data:
        anim = "animations/Stand/Gestures/ShowTablet_1"
    else:
        anim= "animations/Stand/BodyTalk/BodyTalk_" +  str(random.choice(available_bodyTalk))
    print(anim)
    try:
        resp = execute_animation(anim).ack
        if resp!= 'ACK':
            print("There is an error in msg, maybe")
    except rospy.ServiceException as e:
        print("Service call failed: %s", e)
    
def listener():
    rospy.Subscriber("toSpeech", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()