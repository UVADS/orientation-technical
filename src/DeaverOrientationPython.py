#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:33:17 2022

@author: juliadeaver
"""

import matplotlib.pyplot as plt
import pandas as pd

print("Hello World")

url = 'https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv'


df = pd.read_csv(url)
x = df["Operating System"]
plt.hist(x,color="blue")
plt.title("Histogram of Computer Type Frequency")
plt.style.use('ggplot')
plt.show()


x1 = df["GPU (short description as a string)"]
plt.hist(x1,color = "purple")
plt.title("Histogram of GPU type")
plt.style.use('ggplot')
plt.xticks(rotation="vertical")
plt.show()


x2 = df["RAM (in GB)"]
plt.hist(x2,bins=50,color="pink")
plt.title("RAM (in GB) vs frequency in MSDS2023")
plt.style.use('ggplot')
plt.xticks(rotation="vertical")
plt.show()


url2 = "https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2021-06-15-survey.csv"
df2 = pd.read_csv(url2)

# df2.loc[df2["Operating System"]!="Windows 10","Operating System 1"] = 
df2.loc[df2["Operating System"]=="Windows 10","Operating System"] = "Windows"

x3 = df2["Operating System"]
plt.hist(x,label='Class of 2023',alpha=0.5, color  ="pink")
plt.hist(x3, label='Class of 2022',alpha=0.8, color="orange")
plt.legend(loc='upper right')
plt.title("Operating System Frequencies in Class of 2022 vs 2023")
plt.show()