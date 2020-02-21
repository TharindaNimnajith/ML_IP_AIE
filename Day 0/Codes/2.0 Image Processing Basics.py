import cv2  #openCV library

#loading an image
img = cv2.imread('Samples/flower.jpg')  #imread() -> image read
#An image can be represented as a 2D array
#Hence, img is a 2D array

print(img);

print(img[200][200])  #[Blue, Green, Red]

img[200][200] = [255, 255, 255] #white

img[200:205, 200:210] = [255, 2, 25]

#cv2.rectangle(place to draw the rectangle, starting point, ending point, colour, width of the line in pixels)
cv2.rectangle(img, (40, 40), (140, 140), (0, 255, 0), 2)

#cv2.putText(source, text, initializing point, font, font size, colour, thickness)
cv2.putText(img, 'RECTANGLE1', (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

cv2.imshow('FLOWER', img)  #imshow() -> image show
