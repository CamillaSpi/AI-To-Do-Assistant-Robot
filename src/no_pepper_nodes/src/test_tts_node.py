#!/usr/bin/python3


from pepper_nodes.srv import Text2Speech
import rospy

def handle_speech(req):
    print('Speech ',req)
    return 'ACK'

def tts_server():
    rospy.init_node('tts_service')
    s = rospy.Service('tts', Text2Speech, handle_speech)
    rospy.loginfo("talk")
    rospy.spin()

if __name__ == "__main__":
    tts_server()

