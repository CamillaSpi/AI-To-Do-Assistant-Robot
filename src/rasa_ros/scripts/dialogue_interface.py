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
    message.msg = "add run in gym"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "update the activity named run in gym into walk"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "set walk in gym as completed"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "set walk in gym as uncompleted"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "add the category personal"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "modify the category personal in category university"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "yes"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "remove the category university"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "yes"
    dialogue_service(message.msg,message.id) 
    message.msg = "clean completed activity"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "yes"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "show my activities"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "show my categories"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "remind me to call john in personal for yesterday"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "remove walk in gym"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "yes"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "add study in personal for today"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "no"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "modify the activity named study in personal with the name play"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "yes"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "today"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "modify the deadline of the activity play in personal"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "from today to now"
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)
    message.msg = "remind me to breath in personal in 20 seconds"
    dialogue_service(message.msg,message.id) 




def main():
    rospy.init_node('writing')
    rospy.wait_for_service('dialogue_server')
    # testFunction()
    message = RecognizedSpoke()  
    message.msg = "/session_start"
    message.id = -1
    dialogue_service(message.msg,message.id) 
    time.sleep(0.5)


    while not rospy.is_shutdown():
        message = rospy.wait_for_message("text2answer",RecognizedSpoke)
        print("messaggio arrivato nel dialogue interface: ", message)
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