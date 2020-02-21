import cv2

car_clsfr=cv2.CascadeClassifier('Cascades/Vehicle and pedestrain detection/two_wheeler.xml')

capture=cv2.VideoCapture('Sample Videos/bikes.mp4')

bike_img=cv2.imread('bike.png')
(height,width)=bike_img.shape[:2]
bike_img=cv2.resize(bike_img,(int(width/25),int(height/25)))
(bike_height,bike_width)=bike_img.shape[:2]

#cv2.imshow('bike',bike_img)

count=0

while(True):

    ret,img=capture.read()

    (height,width)=img.shape[:2]
    img=cv2.resize(img,(int(width/2),int(height/2)))
    (height,width)=img.shape[:2]

    img[0:30,0:width]=[0,0,255]
    img[0:bike_height,0:bike_width]=bike_img

    blur=cv2.blur(img,(7,7))
    gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    cars=car_clsfr.detectMultiScale(gray)

    cv2.line(img,(0,height-50),(width,height-50),(0,255,0),2)
    
    for (x,y,w,h) in cars:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.rectangle(img,(x-1,y-10),(x+w+1,y),(0,255,255),-1)
        cv2.putText(img,'Motorbike',(x,y-2),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,255),2)

        if((y+h)<(height-47) and (y+h)>(height-53)):

            count=count+1
            cv2.line(img,(0,height-50),(width,height-50),(0,0,255),2)
        
    cv2.putText(img,str(count),(bike_width+20,bike_height-5),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow('LIVE',img)
    cv2.waitKey(1)
