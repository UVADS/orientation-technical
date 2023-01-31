#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:01:23 2022

@author: annedarong

UVA MSDS Technical Orientation 2022 

"""

import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2021-06-15-survey.csv'
df = pd.read_csv(url)
print(df.head(5))

#exclude timestamp, not interested in that variable 

#quantitative columns (4 columns)
quantitative_df = df[['CPU Cycle Rate (in GHz)',
                   'CPU Number of Cores',
                   'RAM (in GB)',
                   'Hard Drive Size (in GB)']]
#histograms 
#calls matplotlib.pyplot.hist()
quantitative_df.hist()


#############################################

#qualitative columns (2 columns)
qualitative_df = df[['Operating System',
                     'GPU (short description)']]

#transform strings
#qualitative_df['GPU (short description)'] = qualitative_df['GPU (short description)'].str.lower()

#for i in quantitative_df:
#    plt.hist(quantitative_df[i])
#    plt.show()
    
#counts
#op_system_counts = qualitative_df['Operating System'].value_counts()
#gpu_counts = qualitative_df['GPU (short description)'].value_counts()
#
##bar plots
#op_system_counts.plot.bar()
#gpu_counts.plot.bar()


