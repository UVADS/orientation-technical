#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:20:29 2022

@author: mj
"""

import pandas as pd 
dat = pd.read_csv('2022-06-14-survey.csv')

import matplotlib.pyplot as plt


plt.hist(dat['CPU Cycle Rate (in GHz)'], edgecolor = "white", color = "purple", 
         bins = 10)
plt.title('CPU Cycle Rate')
plt.xlabel('GHz')
plt.ylabel('Count')



#plt.scatter(dat['CPU Cycle Rate (in GHz)'], dat['CPU Number of Cores (int)'], 
#            color = "orange")
#plt.title('CPU Cycle Rate vs Number of Cores')
#plt.xlabel('Cycle Rate (GHz)')
#plt.ylabel('Number of Cores (int)')