import cv2

#img is a 2D array
#As this is a colour image, there is a 24 bit number in every element
img = cv2.imread('Samples 1/flower.jpg')

#Converting BGR to Gray Scale
#As this is a gray scale image, there is a 8 bit number in every element
#Ggray is also a 2D array
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img[100][100])  #three values in one element (three 8 bits)
print(gray[100][100]) #one value in one element (8 bits)

#printing dimentions / resolution in gray image
(height, width) = gray.shape
print(height, width)

#printing dimentions / resolution in colour image
(height, width, a) = img.shape
print(height, width, a)

import random

for i in range(100):
    r = random.randint(0, height - 1)
    c = random.randint(0, width - 1)
    #r & c are random values
    gray[r][c] = 255
    #artificially creating noice (salt / pepper noice)

#noice removal by bluring (blur function / gaussian blur function)
blur = cv2.blur(gray, (5, 5)) #(5, 5) is the kernal size

#Thresholding - converting gray image to black & white image
ret, bw = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)
#ret -> returning a boolean value (0 - if successful, 1 - if not successful)
#parameters -> source image, threshold value, upper limit, thresholding algorithm
#gray value > 100 converted to 255(white)
#gray value < 100 converted to 0(white)

cv2.imshow('IMG', img)
cv2.imshow('GREY', gray)
cv2.imshow('BLUR', blur)
cv2.imshow('BW', bw)
