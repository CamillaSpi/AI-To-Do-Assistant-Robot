#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from rasa_ros.srv import Dialogue, DialogueResponse
from ros_audio_pkg.msg import RecognizedSpoke
import time

pub = rospy.Publisher('toSpeech', String, queue_size=10)
pub2 = rospy.Publisher("toShow", String,  queue_size=10)

class TerminalInterface:
    '''Class implementing a terminal i/o interface. 

    Methods
    - get_text(self): return a string read from the terminal
    - set_text(self, text): prints the text on the terminal

    '''

    def get_text(self):
        return input("[IN]:  ") 

    def set_text(self,text,id):
        if text.answer[0:2] == '-1':
            pub2.publish('www.google.it')
            text.answer = text.answer[2:]
        elif text.answer[0:2] == '-2':
            pub2.publish('www.google.it')
            text.answer = text.answer[2:]
        pub.publish(text.answer)

dialogue_service = rospy.ServiceProxy('dialogue_server', Dialogue)
terminal = TerminalInterface()
def testFunction():
    message = RecognizedSpoke()  
    message.msg = "Hi i am Vito"
    message.id = 5
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    time.sleep(0.5)
    message.msg = "show my activities"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    time.sleep(0.5)
    message.msg = "clean activity"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    time.sleep(0.5)
    message.msg = "yes"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    time.sleep(0.5)

def main():
    rospy.init_node('writing')
    rospy.wait_for_service('dialogue_server')
    testFunction()

    while not rospy.is_shutdown():
        message = rospy.wait_for_message("text2answer",RecognizedSpoke)
        if message == 'exit': 
            break
        try:
            bot_answer = dialogue_service(message.msg,message.id)
            print('risposta ricevuta')
            terminal.set_text(bot_answer,message.id)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException:
        pass