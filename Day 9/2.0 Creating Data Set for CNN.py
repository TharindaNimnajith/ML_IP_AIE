#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

categories=['Cat','Dog']

train_data=[]
train_target=[]

size=50

for i in range (0,12500):
    
    try:
    
        for category in categories:
        
        
            img=cv2.imread('PetImages/'+category+'/'+str(i)+'.jpg')
            
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            resized=cv2.resize(gray,(size,size))
        
        
            if(category=='Cat'):
            
                train_data.append(resized)
                train_target.append([1,0])
            
            else:
                train_data.append(resized)
                train_target.append([0,1])
    
    except Exception as e:
        
        
        pass
    



        


# In[14]:


print('Length of train data:',len(train_target))
    
import numpy as np

train_data=np.array(train_data)
train_data=train_data.reshape(-1,size,size,1)


train_target=np.array(train_target)


import pickle

pickle.dump(train_data,open('train_data.pickle','wb'))
pickle.dump(train_target,open('train_target.pickle','wb'))


# In[ ]:




