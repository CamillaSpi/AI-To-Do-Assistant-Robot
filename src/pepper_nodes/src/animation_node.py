#!/usr/bin/python3
from utils import Session
from pepper_nodes.srv import Animation
from optparse import OptionParser
import rospy

'''
This class implements a ROS node able call animation service of the robot
'''
class AnimationNode:
    
    '''
    The costructor creates a session to Pepper and inizializes the services
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.session = Session(ip, port)
        self.tts = self.session.get_service("ALAnimationPlayer")
     
    '''
    Rececives a Animation message and call the ALAnimationPlayer service.
    The robot will play the text of the message
    '''
    def say(self, msg):
        try:
            self.tts.say(msg.animation)
        except:
            self.session.reconnect()
            self.tts = self.session.get_service("ALAnimationPlayer")
            self.tts.say(msg.animation)
        return "ACK"
    
    '''
    Starts the node and create the tts service
    '''
    def start(self):
        rospy.init_node("animation_node")
        rospy.Service('tts', Animation, self.say)

        rospy.spin()

if __name__ == "__main__":
    import time
    time.sleep(3)
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    try:
        ttsnode = AnimationNode(options.ip, int(options.port))
        ttsnode.start()
    except rospy.ROSInterruptException:
        pass
