import cv2

camera = cv2.VideoCapture(0)  #0 -> default camera (web cam)

#ret, img = camera.read() #ret is for checking the availability of the camera

while(True):  #infinite loop
    ret, img = camera.read()
    cv2.imshow('LIVE', img)
    cv2.waitKey(10)  #10ms delay
