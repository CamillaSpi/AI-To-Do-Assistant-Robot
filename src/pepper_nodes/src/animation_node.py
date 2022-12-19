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
        self.animation = self.session.get_service("ALAnimationPlayer")
     
    '''
    Rececives a Animation message and call the ALAnimationPlayer service.
    The robot will play the text of the message
    '''
    def run(self, msg):
        try:
            self.animation.run(msg.animation)
        except:
            self.session.reconnect()
            self.animation = self.session.get_service("ALAnimationPlayer")
            self.animation.run(msg.animation)
        return "ACK"
    
    '''
    Starts the node and create the animation service
    '''
    def start(self):
        rospy.init_node("animation_node")
        rospy.Service('animation_node', Animation, self.run)

        rospy.spin()

if __name__ == "__main__":
    import time
    time.sleep(3)
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    try:
        animationnode = AnimationNode(options.ip, int(options.port))
        animationnode.start()
    except rospy.ROSInterruptException:
        pass
