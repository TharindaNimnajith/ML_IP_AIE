import cv2
import imutils #image utilities library
from imutils import face_utils

camera=cv2.VideoCapture(0)      #0 for default camera

import dlib

face_detector=dlib.get_frontal_face_detector()
#classifer for detecting face
landmarks_detector=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#classifer for detecting 68 landmarks in a face

while(True):

    ret,img=camera.read()   #reading a single frame and save it to img
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    rect=face_detector(gray)

    try:
        
        #x1=rect[0].left()
        #y1=rect[0].top()
        #x2=rect[0].right()
        #y2=rect[0].bottom()

        #cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

        points=landmarks_detector(gray,rect[0])

        points=face_utils.shape_to_np(points)   #converting the 68 points into a numpy array

        k=0
        
        for (x,y) in points:

            cv2.circle(img,(x,y),2,(0,0,255),-1)
            cv2.putText(img,str(k),(x-10,y),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,255,255),1)
            #-1 filled circle, otherwise 1,2,3,.... to the width of the curve
            k=k+1
            
        
        cv2.imshow('LIVE',img)
        cv2.waitKey(1)          #1ms pause, allowing time to camera to get another frame


    except Exception as e:
        print(e)    
