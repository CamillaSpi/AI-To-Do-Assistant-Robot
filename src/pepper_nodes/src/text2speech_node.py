#!/usr/bin/python3
from utils import Session
from pepper_nodes.srv import Text2Speech
from optparse import OptionParser
import rospy

'''
This class implements a ROS node able to call the Text to speech service of the robot
'''
class Text2SpeechNode:
    
    '''
    The costructor creates a session to Pepper and inizializes the services
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.session = Session(ip, port)
        self.tts = self.session.get_service("ALTextToSpeech")
     
    '''
    Rececives a Text2Speech message and call the ALTextToSpeech service.
    The robot will play the text of the message
    '''
    def say(self, msg):
        try:
            self.tts.say(msg.speech)
        except:
            self.session.reconnect()
            self.tts = self.session.get_service("ALTextToSpeech")
            self.tts.say(msg.speech)
        return "ACK"
    
    '''
    Starts the node and create the tts service
    '''
    def start(self):
        rospy.init_node("text2speech_node")
        rospy.Service('tts', Text2Speech, self.say)

        rospy.spin()

if __name__ == "__main__":
    import time
    time.sleep(3)
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    try:
        ttsnode = Text2SpeechNode(options.ip, int(options.port))
        ttsnode.start()
    except rospy.ROSInterruptException:
        pass
