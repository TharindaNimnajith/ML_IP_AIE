import cv2
import imutils #image utilities library
from imutils import face_utils
import dlib

face_detector=dlib.get_frontal_face_detector()
landmarks_detector=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

train_data=[[0 for x in range(5)] for y in range(60)]
train_target=[0 for x in range(60)]

img_shapes=['Diamond','Oblong','Oval','Round','Square','Triangle']

count=0

def append_data(points,shape):

    face_dic={'Diamond':0,'Oblong':1,'Oval':2,'Round':3,'Square':4,'Triangle':5}
    
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

    global count
    global train_data
    global train_target

    train_data[count][0]=round(D1,4)
    train_data[count][1]=round(D2,4)
    train_data[count][2]=round(D3,4)
    train_data[count][3]=round(D4,4)
    train_data[count][4]=round(D5,4)

    train_target[count]=face_dic[shape]

    count=count+1
    
for num in range(0,10):

    for shape in img_shapes:

        img=cv2.imread('Face Shapes/'+shape+'/'+str(num+1)+'.jpeg')
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        rect=face_detector(gray)

        points=landmarks_detector(gray,rect[0])
        points=face_utils.shape_to_np(points)

        append_data(points,shape)

import pickle #can write arrays directly into files
import numpy as np

train_data=np.array(train_data)
train_target=np.array(train_target)

train_data_file=open('train_data.pickle','wb')
train_target_file=open('train_target.pickle','wb')

#dump for write

pickle.dump(train_data,train_data_file)
pickle.dump(train_target,train_target_file)

train_data_file.close()
train_target_file.close()
