#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pickle

train_data_file = open('train_data.pickle', 'rb')
train_target_file = open('train_target.pickle', 'rb')

train_data = pickle.load(train_data_file)
train_target = pickle.load(train_target_file)

#train_data=pickle.load(open('train_data.pickle','rb'))
#train_target=pickle.load(open('train_target.pickle','rb'))

print(train_data.shape)
print(train_target.shape)

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten
from tensorflow.keras.layers import Conv2D,MaxPooling2D


# In[15]:


train_data = train_data / 255.0
#scale down 0-255 to 0-1

model = Sequential()

model.add(Conv2D(256, (3,3), input_shape = train_data.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))

model.add(Flatten())

model.add(Dense(64, activation = 'relu'))
#model.add(Dense(64))
#model.add(Activation('relu'))

model.add(Dense(2, activation = 'softmax'))
#model.add(Dense(2))
#model.add(Activation('softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
#changes that can be made:-
#loss
#optimizer = 'sgd'
#batch_size
#no of epochs


# In[ ]:


model.fit(train_data, train_target, batch_size = 32, epochs = 3)


# In[ ]:


model.save_weights('CNN_Cats_Dogs_test.h5')

