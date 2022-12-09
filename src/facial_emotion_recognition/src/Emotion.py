import numpy as np
import cv2
import tensorflow as tf

def getFaceBox(net, frame, conf_threshold=0.8):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    
    #swapRB =True
    # flag which indicates that swap first and last channels in 3-channel image is necessary.
    #crop = False
    # flag which indicates whether image will be cropped after resize or not
    # If crop is false, direct resize without cropping and preserving aspect ratio is performed
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold and detections[0, 0, i, 5]<1 and detections[0, 0, i, 6]<1:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/300)), 8)
    return frameOpencvDnn, bboxes


# Initialize detector
faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"

faceNet = cv2.dnn.readNet(faceModel, faceProto)

# Initialize emotion classifier
from tensorflow.keras.models import load_model
emotionModel = "emotion.hdf5"
emotionNet = load_model(emotionModel)
emotionList = ['surprise','fear','disgust','happiness','sadness','anger','neutral']
padding = 0.2
MEANS=np.array([131.0912, 103.8827, 91.4953])
INPUT_SIZE = (224,224)


# Read frame 
#version for acquire frame from camera
#cap = cv2.VideoCapture(0)
#while(1):
frame = cv2.imread('test1.jpg')                     # Read frame
#_,frame = cap.read()                    # Read frame
frameFace, bboxes = getFaceBox(faceNet, frame)     # Get face
print(bboxes)
print(frameFace)

for i,bbox in enumerate(bboxes):
    # Adjust crop
    print("frame face",i,frameFace[i])
    w = bbox[2]-bbox[0]
    h = bbox[3]-bbox[1]
    padding_px = int(padding*max(h,w))
    face = frame[max(0,bbox[1]-padding_px):min(bbox[3]+padding_px,frame.shape[0]-1),max(0,bbox[0]-padding_px):min(bbox[2]+padding_px, frame.shape[1]-1)]
    face = face[ face.shape[0]//2 - face.shape[1]//2 : face.shape[0]//2 + face.shape[1]//2, :, :]
    # Preprocess image
    resized_face = cv2.resize(face,INPUT_SIZE)
    blob = np.array([resized_face.astype(float)-MEANS])
    # Predict
    emotionPreds = emotionNet.predict(blob)
    print(emotionPreds)
    # Draw
    #cv2.imshow("f%d"%i, resized_face)
    #cv2.moveWindow("f%d"%i, INPUT_SIZE[0]*i, 40)
    print(".2f"%c for c in emotionPreds)
    emotion = emotionList[emotionPreds[0].argmax()]
    cv2.imshow("frameface",frameFace)
    #cv2.putText(frameFace, emotion, (bbox[0]+w//20, bbox[1]+h//20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow("Emotion Demo", frameFace)
cv2.waitKey(0)
cv2.destroyAllWindows()
