import cv2

classifier = cv2.CascadeClassifier('Cascades/Face & Eyes/haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)

ret = 1

while(ret == 1):
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = classifier.detectMultiScale(gray)
    
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 255, 0), 2)
    
    cv2.imshow('LIVE', frame)
    cv2.waitKey(1)





