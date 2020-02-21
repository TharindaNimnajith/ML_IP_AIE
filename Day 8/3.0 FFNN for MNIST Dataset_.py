#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tensorflow as tf

mnist = tf.keras.datasets.mnist

(train_data, train_target), (test_data, test_target) = mnist.load_data()


# In[8]:


from matplotlib import pyplot as plt

plt.imshow(train_data[0], cmap = 'binary')
plt.show()


# In[14]:


#import keras.models as models
#import keras.layers as layers

import tensorflow.keras.models as models
import tensorflow.keras.layers as layers


# In[ ]:


model = models.Sequential()

model.add(layers.Flatten(input_shape = (28, 28)))

