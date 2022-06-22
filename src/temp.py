# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r'/Users/Christine/Downloads/orientation-technical-main/dat/2022-06-14-survey.csv')
for col in data.columns:
    print(col)
list(data.columns) 
print(data.head())

CPU_GPU = data[["CPU Number of Cores (int)", "GPU CUDA Number of Cores (int)"]]
print(CPU_GPU.head())
hist = CPU_GPU.hist(bins=10)


