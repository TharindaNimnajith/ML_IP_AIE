#!/usr/bin/env python
# coding: utf-8

# In[9]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D


# In[10]:


model = Sequential()

model.add(Conv2D(256, (3,3), input_shape = (50, 50, 1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())
model.add(Dense(64, activation = 'relu'))
model.add(Dense(2, activation = 'softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])


# In[11]:


model.load_weights('CNN_Cats_Dogs.h5')


# In[14]:


import cv2

video = cv2.VideoCapture('video.mp4')

ret = 1

while(ret == 1):
    ret, frame = video.read()
    frame = cv2.resize(frame, (600, 350))
    
    test_data = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    test_data = cv2.resize(test_data, (50, 50))
    
    test_data = test_data.reshape(-1, 50, 50, 1)
    test_data = test_data / 255.0
    
    result = model.predict(test_data)
    
    #print(result)
    
    result = np.array(result[0] * 100)
    
    prob = 'CAT: ' + str(round(result[0], 1) + '%  DOG: ' + str(round(result[1], 1)) + '%'
    
    cv2.putText(frame, prob, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    cv2.imshow('LIVE', frame)
    cv2.waitKey(100)


# In[ ]:





# In[ ]:




