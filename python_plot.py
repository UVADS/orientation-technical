# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:59:31 2022

@author: ljd3frf
"""
import matplotlib.pyplot as plt
import pandas as pd

dat = pd.read_csv("https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv")
dat = dat[dat['CPU Cycle Rate (in GHz)'] < 256]
#%%
plt.hist(dat.loc[:,"CPU Cycle Rate (in GHz)"],bins = 10)
plt.title('CPU Cycle Rate (in GHz)')
plt.xlabel('Cycle rate (GHz)')
plt.ylabel('Count')
