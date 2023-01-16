#!/usr/bin/python3


from pepper_nodes.srv import LoadUrl
import rospy

def handle_speech(req):
    print("I'm sending to tablet ", req)
    return 'ACK'

def url_server():
    rospy.init_node('url_service')
    s = rospy.Service('load_url', LoadUrl, handle_speech)
    rospy.loginfo("url")
    rospy.spin()

if __name__ == "__main__":
    url_server()

