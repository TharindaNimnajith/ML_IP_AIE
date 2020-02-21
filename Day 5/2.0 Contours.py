import cv2

image = cv2.imread('Materials/gray_image.png')

blur = cv2.blur(image, (3, 3))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(gray, 76, 255, cv2.THRESH_BINARY)

ret, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image, [contours[1]], 0, (0, 255, 0), 2)

for cont in contours:
    cv2.drawContours(image, [cont], 0, (0, 255, 0), 2)

cv2.imshow('IMAGE', image)
##cv2.imshow('BLUR', blur)
##cv2.imshow('GRAY', gray)
cv2.imshow('THRESHOLD', threshold)
