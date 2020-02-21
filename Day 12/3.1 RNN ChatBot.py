#!/usr/bin/env python
# coding: utf-8

# In[12]:


from gensim.models import Word2Vec, KeyedVectors
model = KeyedVectors.load_word2vec_format('E:\SLIIT\Machine Learning (ML) & Image Processing (IP)\Day 12\GoogleNews-vectors-negative300.bin', binary = True, limit = 100000)

import json
dataset = json.load(open('E:\SLIIT\Machine Learning (ML) & Image Processing (IP)\Day 12\conversation.json'))

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


# In[13]:


data[0]


# In[14]:


target[0]


# In[15]:


print(data[0])


# In[16]:


print(target[0])


# In[17]:


from nltk import word_tokenize


# In[18]:


tok_data = word_tokenize(data[0])

print(tok_data)


# In[ ]:




