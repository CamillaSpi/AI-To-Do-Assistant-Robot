#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from rasa_ros.srv import Dialogue, DialogueResponse

pub = rospy.Publisher('toSpeech', String, queue_size=10)

class TerminalInterface:
    '''Class implementing a terminal i/o interface. 

    Methods
    - get_text(self): return a string read from the terminal
    - set_text(self, text): prints the text on the terminal

    '''

    def get_text(self):
        return input("[IN]:  ") 

    def set_text(self,text):
        pub.publish(text)
        print("[OUT]:",text)

def main():
    rospy.init_node('writing')
    rospy.wait_for_service('dialogue_server')
    dialogue_service = rospy.ServiceProxy('dialogue_server', Dialogue)

    terminal = TerminalInterface()

    while not rospy.is_shutdown():
        message = rospy.wait_for_message("spoken_text",String)
        if message == 'exit': 
            break
        try:
            bot_answer = dialogue_service(message.data)
            terminal.set_text(bot_answer.answer)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

if __name__ == '__main__':
    try: 
        main()
    except rospy.ROSInterruptException:
        pass