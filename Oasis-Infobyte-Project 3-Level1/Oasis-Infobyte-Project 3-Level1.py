#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import pandas as pd
df = pd.read_csv(r"C:\Users\kumar\Downloads\Oasis infobyte internship\Data cleaning\Oasis-Infobyte-Project 3-Level1\AB_NYC_2019.csv")
df.head() 


# In[7]:


to_drop = ['last_review',
           'neighbourhood']

df.drop(to_drop, inplace=True, axis=1)


# In[9]:


df.head()


# In[10]:


df.drop(columns=to_drop, inplace=True)


# In[13]:


df['host_id'].is_unique


# In[14]:


df = df.set_index('host_name')
df.head()


# In[16]:


df.set_index('room_type', inplace=True)


# In[22]:


df['reviews_per_month'].head(10)


# In[25]:


pub = df['neighbourhood_group']
neighbourhood = pub.str.contains('neighbourhood')
neighbourhood[:5]


# In[26]:


df['neighbourhood_group'].head()


# In[27]:


df.head()


# In[ ]:




