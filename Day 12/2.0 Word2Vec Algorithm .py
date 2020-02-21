#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Read csv, excel etc. files to python
import pandas as pd


# In[ ]:


df = pd.read_csv('reddit_worldnews_start_to_2016-11-22.csv')


# In[ ]:


df.head(1000)


# In[ ]:


news_titles = df['title'].values


# In[ ]:


news_titles


# In[ ]:


print(news_titles)


# In[ ]:


import nltk


# In[ ]:


nltk.download('punkt')


# In[ ]:


ex1 = nltk.word_tokenize(news_titles[0])


# In[ ]:


print(news_titles[0])


# In[ ]:


print(ex1)


# In[ ]:


sentence = 'I want to go home'
words = nltk.word_tokenize(sentence)


# In[ ]:


print(sentence)


# In[ ]:


sentence


# In[ ]:


print(words)


# In[ ]:


words


# In[ ]:


print(len(words))


# In[ ]:


len(words)


# In[ ]:


news_vector = [nltk.word_tokenize(title) for title in news_titles]


# In[ ]:


print(news_vector[:10])


# In[ ]:


news_vector[:10]


# In[ ]:


print(news_vector)


# In[ ]:


news_vector


# In[ ]:


from gensim.models import Word2Vec


# In[ ]:


model.Word2Vec(news_vector, min_count = 1, size = 32)


# In[ ]:


model['pakistan']


# In[ ]:


model['King']


# In[ ]:


model['Man']


# In[ ]:


model['Woman']


# In[ ]:


model['Queen']


# In[ ]:


vector_1 = model['King'] - model['Man'] + model['Woman']


# In[ ]:


model.most_similar([vector_1])


# In[ ]:


vector_1


# In[ ]:


print(vector_1)


# In[ ]:


vector_1 = model.wv['King'] - model.wv['Man'] + model.wv['Woman']


# In[ ]:


model.wv.most_similar([vector_1])


# In[ ]:




