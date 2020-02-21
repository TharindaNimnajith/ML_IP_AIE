#!/usr/bin/env python
# coding: utf-8

# In[23]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
#from tensorflow.keras.models import Sequential
#keras is a high level API for tensorflow
from keras import models #models - Neural Networks
from keras import layers #layers - Neural Network Layers (input layer, hidden layers, output layer)
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils

iris = load_iris()

data = iris.data
target = iris.target

train_data, test_data, train_target, test_target = train_test_split(data, target, test_size = 0.1)

model = models.Sequential() #model is a FFNN (Feed Forward Neural Network)

model.add(layers.Dense(8, input_dim = 4, activation = 'relu')) #Dense layer is a fully connected layer
model.add(layers.Dense(8, input_dim = 8, activation = 'relu'))
model.add(layers.Dense(3, input_dim = 8, activation = 'softmax'))

#model.compile(loss = 'categorical_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
#sgd - sequential gradient descent
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

encoder = LabelEncoder()
encoder.fit(train_target)

train_target = encoder.transform(train_target)
train_target = np_utils.to_categorical(train_target)

model.fit(train_data, train_target, epochs = 100)


# In[24]:


results = model.predict(test_data)
print(results)


# In[25]:


print(results[0])
print(test_target[0])


# In[26]:


print(results[1])
print(test_target[1])


# In[27]:


print(results)
print(test_target)


# In[28]:


import numpy as np

print(np.argmax(results, axis = 1))
print(test_target)


# In[ ]:




