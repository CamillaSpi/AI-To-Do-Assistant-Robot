#!/usr/bin/python3
from utils import Session
from optparse import OptionParser
import rospy
from pepper_nodes.srv import WakeUp, Rest

'''
This class implements a ROS node used to controll the Pepper posture
'''
class WakeUpNode:
    
    '''
    The costructor creates a session to Pepper and inizializes the services
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.session = Session(ip, port)
        self.motion_proxy = self.session.get_service("ALMotion")
        self.posture_proxy = self.session.get_service("ALRobotPosture")
    
    '''
    This method calls the ALMotion service and sets the robot to rest position
    '''
    def rest(self, *args):
        try:
            self.motion_proxy.rest()
        except:
            self.motion_proxy = self.session.get_service("ALMotion")
            self.motion_proxy.rest()
        return "ACK"
    
    '''
    This method calls the ALMotion and ALRobotPosture services and it sets motors on and then it sets the robot posture to initial position
    '''
    def wakeup(self, *args):
        try:
            self.motion_proxy.wakeUp()
            self.stand()
        except:
            self.motion_proxy = self.session.get_service("ALMotion")
            self.posture_proxy = self.session.get_service("ALRobotPosture")
            self.motion_proxy.wakeUp()
            self.stand()         

        return "ACK"   
    
    '''
    This method sets the robot posture to "StandInit" posture
    '''
    def stand(self, *args):
        self.posture_proxy.goToPosture("StandInit", 0.5)
    
    '''
    Starts the node and wake up the robot
    '''
    def start(self):
        rospy.init_node("wakeup_node")
        self.wakeup()
        self.stand()        
        rospy.Service("wakeup", WakeUp, self.wakeup)
        rospy.Service("rest", Rest, self.rest)
        rospy.spin()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    try:
        node = WakeUpNode(options.ip, int(options.port))
        node.start()
    except rospy.ROSInterruptException:
        pass
