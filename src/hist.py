# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import the pandas library for data manipulation and plt for plotting.
import pandas as pd
import matplotlib.pyplot as plt

# Label the X and Y variables for the histogram.
plt.xlabel('RAM')
plt.ylabel('Frequency')

# Read and display data frames
df = pd.read_csv (r"C:\Users\duxvo\OneDrive\Documents\2022-06-14-survey.csv")
plt.hist(df['RAM (in GB)']) 
plt.title('Histogram of RAM')
df = df[df['RAM (in GB)' < 200 ]]
df.columns
print(df);