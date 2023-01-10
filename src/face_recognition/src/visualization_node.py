#!/usr/bin/env python3
import rospy
from vision_msgs.msg import Detection2DArray
import cv2
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy


rospy.init_node('visualization_node')

labelConversation = {
    0:'nando',
    1:'vito',
    2:'camila',
    3:'mattia'
}

def rcv_identity(msg):
    global image
    #rospy.loginfo('detection here')
    frame_face = None
    for d in msg.detections:
        if (frame_face is None):
            frame_face = ros_numpy.numpify(d.source_img)
        id = d.results[0].id
        identity = 'unrecognized user'
        if id < 4:
            identity = labelConversation[id]
        #print(identity)
        cv2.putText(frame_face, identity, (round(d.bbox.center.y-d.bbox.size_y/2+d.bbox.size_x //20), round(d.bbox.center.x-d.bbox.size_x/2+d.bbox.size_y//20)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("identity Demo", frame_face)
    
    cv2.waitKey(5)


sd = rospy.Subscriber("identity", Detection2DArray, rcv_identity)


try:
    rospy.spin()

except KeyboardInterrupt:
    print("Shutting down")