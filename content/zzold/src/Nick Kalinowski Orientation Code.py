#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[9]:


survey_data = pd.read_csv("2022-06-14-survey.csv")


# In[10]:


survey_data = survey_data[survey_data.iloc[: , 2] < 500]


# In[11]:


survey_data


# In[28]:


plt.hist(survey_data.iloc[: , 2], bins = 15)

plt.xlabel('Cycle Rate', fontweight ='bold', fontsize = 15)
plt.ylabel('Frequency', fontweight ='bold', fontsize = 15)
plt.title('Cycle Rate Histogram', fontweight = 'bold', fontsize = 20)

plt.show()


# In[30]:


survey_data.columns = ['Timestamp', 'OS', 'Cycle_Rate', 'Num_cores', 'RAM', 'Hard_drive_size', 'GPU', 'GPU_CUDA']

survey_data.pivot(columns='OS', values='Cycle_Rate').plot.hist(bins = 15, alpha = 0.5)

plt.xlabel('Cycle Rate', fontweight ='bold', fontsize = 15)
plt.ylabel('Frequency', fontweight ='bold', fontsize = 15)
plt.title('Cycle Rate By OS', fontweight = 'bold', fontsize = 20)

plt.show()


# In[ ]:




