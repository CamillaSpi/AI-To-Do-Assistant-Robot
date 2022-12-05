#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from rasa_ros.srv import Dialogue, DialogueResponse
from ros_audio_pkg.msg import RecognizedSpoke

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
            print('rilevato show activity')
            pub2.publish('www.google.it')
            text.answer = text.answer[2:]
        if text.answer[0:2] == '-2':
            print('rilevato show category')
            pub2.publish('www.google.it')
            text.answer = text.answer[2:]
        pub.publish(text.answer)
        print("[OUT]:",text.answer)

dialogue_service = rospy.ServiceProxy('dialogue_server', Dialogue)
terminal = TerminalInterface()
def testFunction():
    message = RecognizedSpoke()  
    message.msg = "Hi i am Vito"
    message.id = 5
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "add run in gym"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "no"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "yes"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "show my activities"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "set run in gym as completed"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "no"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "show my activities"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    # message.msg = "remove all my completed activities"
    # bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "add walk in personal for tomorrow at 10:00"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "yes"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "show my activities"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)
    message.msg = "show my category"
    bot_answer = dialogue_service(message.msg,message.id) 
    terminal.set_text(bot_answer,message.id)

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