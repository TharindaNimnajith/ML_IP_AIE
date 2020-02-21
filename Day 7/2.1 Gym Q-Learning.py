#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gym

env = gym.make('Taxi-v2').env
env.render()


# In[3]:


state = env.encode(3, 1, 2, 0) 
#(taxi row, taxi column, pasenger index, destination index)
#Indexes: R = 0, G = 1, Y = 2, B = 3

env.s = state

env.render()


# In[6]:


env.P #Reward metrix -> 500 x 6


# In[7]:


env.P[0] #(probabily, next state, reward, done)


# In[10]:


import numpy as np

Q = np.zeros([500, 6])

#alpha = 0.1
gamma = 0.6
epsilon = 0.1

done = 0


# In[ ]:


for i in range(10000):
    state = env.reset()
    
    while not done:
        action = np.argmax(Q[state])
        next_state, reward, done, info = env.step(action)
        
        Q[state, action] = reward + gamma * np.max(Q[next_state])
        
print('Training Finished')


# In[ ]:




