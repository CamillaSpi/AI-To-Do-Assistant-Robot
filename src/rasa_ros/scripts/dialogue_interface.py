#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from rasa_ros.srv import Dialogue, DialogueResponse
from ros_audio_pkg.msg import RecognizedSpoke
import time

                                           


dialogue_service = rospy.ServiceProxy('dialogue_server', Dialogue)
def testFunction():
    message = RecognizedSpoke()  
    message.msg = "Hi i am Vito"
    message.id = 5
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "show my activities"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "clean activity"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "yes"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "remind me to walk in gym"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "tomorrow"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)




def main():
    rospy.init_node('writing')
    rospy.wait_for_service('dialogue_server')
    testFunction()

    while not rospy.is_shutdown():
        message = rospy.wait_for_message(" ",RecognizedSpoke)
        if message == 'exit': 
            break
        try:
            dialogue_service(message.msg,message.id)
            print('risposta ricevuta')
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException:
        pass