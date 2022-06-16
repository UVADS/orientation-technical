#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib
import pandas as pd
import matplotlib.pyplot


# In[4]:


data = pd.read_csv("2022-06-14-survey.csv")
data.head()


# In[13]:


subplots(2,2)
matplotlib.pyplot.hist(data['Operating System'],align='mid')
matplotlib.pyplot.title('Operating System')


# In[ ]:




