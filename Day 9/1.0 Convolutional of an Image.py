#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

img=cv2.imread('dog.jpg')

filter1=([[0,-1,-1],
        [-1.0,-1],
        [-1,-1,0]])

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

height,width=gray.shape

filtered_img=np.zeros_like(gray)

SUM=0

for i in range (1,height-2):
    for j in range(1,width-2):
        for x in range (0,3):
            for y in range(0,3):
                
                
                SUM=SUM+(filter1[x][y]*gray[i+x][j+y])
        SUM=SUM/9.0
        filtered_img[i+1][j+1]=SUM
        
        
cv2.imshow('FILTER',filtered_img)
cv2.waitKey(0)


# In[ ]:





# In[ ]:




