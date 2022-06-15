#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:01:33 2022

@author: gunnarfranko
"""

import pandas as pd

data1 = pd.read_csv('https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv')

data1 = data1[data1['Hard Drive Size (in GB)'] < 800]
import matplotlib.pyplot as plt

plt.hist(data1['Hard Drive Size (in GB)'], color='Orange')

plt.title('Hard Drive Size (in GB)')
plt.xlabel('Hard Drive Size')
plt.ylabel('Frequency')


print('hello world')
