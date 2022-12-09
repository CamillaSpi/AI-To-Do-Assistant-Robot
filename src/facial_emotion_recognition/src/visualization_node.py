#!/usr/bin/env python3
import os
import rospy
from sensor_msgs.msg import Image
from vision_msgs.msg import Detection2D, Detection2DArray, ObjectHypothesisWithPose
import cv2
import ros_numpy # pip3 install git+https://github.com/eric-wieser/ros_numpy
from threading import Lock

emotionList = ['surprise','fear','disgust','happiness','sadness','anger','neutral']

rospy.init_node('visualization_node')


def rcv_emotion(msg):
    global image
    rospy.loginfo('detection here')
    # image_lock.acquire()
    # if image is None: im = None
    # else: im = image.copy()
    # image_lock.release()
    # if im is None: return
    # h,w,_ = im.shape
    frame_face = None
    for d in msg.detections:
        if (frame_face is None):
            frame_face = ros_numpy.numpify(d.source_img)
        emotion = emotionList[d.results[0].id]
        cv2.putText(frame_face, emotion, (round(d.bbox.center.y-d.bbox.size_y/2+d.bbox.size_x //20), round(d.bbox.center.x-d.bbox.size_x/2+d.bbox.size_y//20)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("Emotion Demo", frame_face)
    cv2.waitKey(100)
    #cv2.destroyAllWindows()


sd = rospy.Subscriber("emotion", Detection2DArray, rcv_emotion)


try:
    rospy.spin()

except KeyboardInterrupt:
    print("Shutting down")