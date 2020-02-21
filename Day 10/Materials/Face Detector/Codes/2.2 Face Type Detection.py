import pickle

data_file=open('train_data.pickle','rb') #rb-read bytes
target_file=open('train_target.pickle','rb')

#load for read

train_data=pickle.load(data_file)
train_target=pickle.load(target_file)

from sklearn import neighbors

clsfr=neighbors.KNeighborsClassifier()
clsfr.fit(train_data,train_target)


import cv2
import imutils #image utilities library
from imutils import face_utils

camera=cv2.VideoCapture(0)      #0 for default camera

def predict_face(img,points):

    face_dic={0:'Diamond',1:'Oblong',2:'Oval',3:'Round',4:'Square',5:'Triangle'}
    
    point7=[0 for x in range(7)]

    point7[0]=points[2][0]
    point7[1]=points[3][0]
    point7[2]=points[4][0]
    point7[3]=points[5][0]
    point7[4]=points[6][0]
    point7[5]=points[7][0]
    point7[6]=points[8][0]

    d1=point7[6]-point7[0]
    d2=point7[6]-point7[1]
    d3=point7[6]-point7[2]
    d4=point7[6]-point7[3]
    d5=point7[6]-point7[4]
    d6=point7[6]-point7[5]

    D1=d2/float(d1)*100
    D2=d3/float(d1)*100
    D3=d4/float(d1)*100
    D4=d5/float(d1)*100
    D5=d6/float(d1)*100

    result=clsfr.predict([[D1,D2,D3,D4,D5]])
    result=result[0]
    #print(face_dic[result])
    cv2.putText(img,face_dic[result],(280,40),cv2.FONT_HERSHEY_SIMPLEX,1.4,(0,0,255),4)

import dlib

face_detector=dlib.get_frontal_face_detector()
#classifer for detecting face
landmarks_detector=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#classifer for detecting 68 landmarks in a face

while(True):

    ret,img=camera.read()   #reading a single frame and save it to img
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    rect=face_detector(gray)

    img[:50,:]=[0,255,0]
    cv2.putText(img,'FACE TYPE:',(5,40),cv2.FONT_HERSHEY_SIMPLEX,1.4,(255,255,255),4)
    try:

        points=landmarks_detector(gray,rect[0])

        points=face_utils.shape_to_np(points)   #converting the 68 points into a numpy array

        k=0
        
        for (x,y) in points:

            cv2.circle(img,(x,y),2,(0,0,255),-1)
            cv2.putText(img,str(k),(x-10,y),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,255,255),1)
            #-1 filled circle, otherwise 1,2,3,.... to the width of the curve
            k=k+1
        
        predict_face(img,points)   
        cv2.imshow('LIVE',img)
        cv2.waitKey(1)          #1ms pause, allowing time to camera to get another frame


    except Exception as e:
        print(e)    


