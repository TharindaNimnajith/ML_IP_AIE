#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gensim.models import Word2Vec, KeyedVectors


# In[ ]:


model = KeyedVectors.load_word2vec_format('E:\SLIIT\Machine Learning (ML) & Image Processing (IP)\Day 12\GoogleNews-vectors-negative300.bin', binary = True, limit = 100000)


# In[ ]:


model['King']


# In[ ]:


len(model['King'])


# In[ ]:


print(len(model['King']))


# In[ ]:


print(model)


# In[ ]:


vec = model['King'] - model['Man'] + model['Woman']


# In[ ]:


model.most_similar([vec])


# In[ ]:


vec = model['Germany'] - model['Berlin'] + model['Paris']
model.most_similar([vec])


# In[ ]:


model['Pakistan']


# In[ ]:


model['King']


# In[ ]:


model['Man']
model['Woman']
model['Queen']


# In[ ]:


vector_1 = model.wv['King'] - model.wv['Man'] + model.wv['Woman']
model.wv.most_similar([vector_1])
vector_1


# In[ ]:


print(vector_1)


# In[ ]:


vector_1 = model.wv['King'] - model.wv['Man'] + model.wv['Woman']
model.wv.most_similar([vector_1])


# In[62]:


import json


# In[63]:


dataset = json.load(open('E:\SLIIT\Machine Learning (ML) & Image Processing (IP)\Day 12\conversation.json'))


# In[ ]:


dataset


# In[ ]:


len(dataset)


# In[ ]:


print(len(dataset))


# In[ ]:


print(dataset)


# In[ ]:


[dataset]


# In[ ]:


len([dataset])


# In[64]:


data = []
target = []

for i in dataset['conversations']:
    for j in i:
        print(j)


# In[66]:


data = []
target = []

count = 0

for i in dataset['conversations']:
    for j in i:
        if(count % 2 == 0):
            data.append(j)
        else:
            target.append(j)
        
        count = count + 1
        
    count = 0    


# In[ ]:




