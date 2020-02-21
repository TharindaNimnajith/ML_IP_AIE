#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

z = 100000;

y = 1 / (1 + np.exp(-z))

print(y)


# In[2]:


z = -100000;

y = 1 / (1 + np.exp(-z))

print(y)


# In[3]:


import tensorflow


# In[4]:


import keras


# In[8]:


from matplotlib import pyplot as plt


# In[11]:


z = np.arange(-10, 10);

y = 1 / (1 + np.exp(-z))

plt.plot(z, y)
plt.show()


# In[ ]:




