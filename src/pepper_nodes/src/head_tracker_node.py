#!/usr/bin/python3
from utils import Session
from pepper_nodes.srv import Tracker
from optparse import OptionParser
import rospy

'''
This class implements a ROS node able call tracker_service service of the robot
'''
class TrackerNode:
    
    '''
    The costructor creates a session to Pepper and inizializes the services
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.session = Session(ip, port)
        self.tracker_service = self.session.get_service("ALTracker")
     
    '''
    Rececives a Tracker message and call the ALTracker service.
    The robot will play the text of the message
    '''
    def run(self, msg):
        if 'stop' in msg.tracker:
            self.stop()
        else:
            try:
                self.tracker_service.setMode("Head")
                self.tracker_service.track(msg.traker)
            except:
                self.session.reconnect()
                self.tracker_service = self.session.get_service("ALTracker")
                self.tracker_service.track(msg.traker)
            return "ACK"
     
    '''
    Rececives a Tracker message and call the ALTracker service.
    The robot will play the text of the message
    '''
    def stop(self):
        try:
            self.tracker_service.stopTracker()
        except:
            self.session.reconnect()
            self.tracker_service = self.session.get_service("ALTracker")
            self.tracker_service.stopTracker()
        return "ACK"
    
    '''
    Starts the node and create the tracker_service service
    '''
    def start(self):
        rospy.init_node("tracker_service_node")
        rospy.Service('tracker_service_node', Tracker, self.run)

        rospy.spin()

if __name__ == "__main__":
    import time
    time.sleep(3)
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    try:
        tracker_servicenode = TrackerNode(options.ip, int(options.port))
        tracker_servicenode.start()
    except rospy.ROSInterruptException:
        pass
