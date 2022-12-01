#!/usr/bin/python3

from utils import Session
from optparse import OptionParser
import rospy
from pepper_nodes.srv import ExecuteJS, LoadUrl

'''
This class implements a ROS node used to controll the Pepper tablet
'''
class TabletNode:
    
    '''
    The costructor creates a session to Pepper and inizializes the services
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.session = Session(ip, port)
        self.tablet_proxy = self.session.get_service("ALTabletService")
        self.tablet_proxy.resetTablet()
    
    '''
    It receives a LoadUrl message and displays the web page associated with the url on the tablet.
    '''
    def load_url(self, msg):
        try:
            self.tablet_proxy.showWebview(msg.url)
        except:
            self.tablet_proxy = self.session.get_service("ALTabletService")
            self.tablet_proxy.showWebview(msg.url)
        return "ACK"
    
    '''
     It receives a LoadUrl message and executes the javascript on the web browser
    '''
    def execute_js(self, msg):
        try:
            self.tablet_proxy.executeJS(msg.js)
        except:
            self.tablet_proxy = self.session.get_service("ALTabletService")
            self.tablet_proxy.executeJS(msg.js)
            
        return "ACK"
    
    '''
    Starts the node and creates the services
    '''
    def start(self):
        rospy.init_node("tablet_node")

        rospy.Service('execute_js', ExecuteJS, self.execute_js)
        rospy.Service('load_url', LoadUrl, self.load_url)

        rospy.spin()

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--ip", dest="ip", default="10.0.1.207")
    parser.add_option("--port", dest="port", default=9559)
    (options, args) = parser.parse_args()

    try:
        node = TabletNode(options.ip, int(options.port))
        node.start()
    except rospy.ROSInterruptException:
        pass
