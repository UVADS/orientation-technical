#!/usr/bin/env python
# coding: utf-8

# In[4]:


print('hello world')

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv')

number_of_cores = df.iloc[:,3]

print(number_of_cores)
number_of_cores.hist()

