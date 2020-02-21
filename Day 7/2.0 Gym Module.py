#!/usr/bin/env python
# coding: utf-8

# In[24]:


import gym

env = gym.make('Taxi-v2').env


# In[25]:


env.render()


# In[33]:


env.P[150]


# In[36]:


env.action_space.sample()
env.step(1)
env.render()


# In[37]:


print(env.action_space)
print(env.observation_space)


# In[ ]:




