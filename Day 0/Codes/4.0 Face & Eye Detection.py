import cv2

camera = cv2.VideoCapture(0)
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

while(True):
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert the img to gray scale
    faces = face_classifier.detectMultiScale(gray)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, 'Tharinda', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
                    
    cv2.imshow('LIVE', img)
    cv2.waitKey(10)

