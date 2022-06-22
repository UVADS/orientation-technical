#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[6]:


from pathlib import Path

#create path to data file
df = Path('/Users/theothormann/Desktop/Data Science/Orientation/Data/2022-06-14-survey.csv')

#read csv
df = pd.read_csv(df)


# In[7]:


#filters outlier
df = df[df.iloc[:,4] <256]


# In[11]:


# Add title and axis names
plt.title('RAM in MSDS Class of 2022 Computers')
plt.xlabel('RAM (in GB)')
plt.ylabel('Number of Responses')
#creates histogram
plt.hist(df.iloc[:,4])

