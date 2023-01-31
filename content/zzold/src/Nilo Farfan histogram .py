# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:43:59 2022

@author: Nilo Farfan
"""
import pandas as pd 
import matplotlib.pyplot as plt
pd.read_csv(r'C:/Users/Nilo Farfan/Desktop/msds survey data.txt')

a = pd.read_csv(r'C:/Users/Nilo Farfan/Desktop/msds survey data.txt')

print (a)

plt.hist(a["Operating System"])

