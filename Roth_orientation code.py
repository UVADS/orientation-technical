# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:00:15 2022
Create a histogram of orientation data with Python

@author: alexandra
"""
##import pandas
import pandas as pd

##create variables for github files
file21 = "https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2021-06-15-survey.csv"
file22 = "https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv"

##read data into new variables
data21 = pd.read_csv(file21)
data22 = pd.read_csv(file22)

##rename columns
data21.columns = ["time", "os", "cpu_cycles", "cpu_cores", "ram", "hd", "gpu"]
data22.columns = ["time", "os", "cpu_cycles", "cpu_cores", "ram", "hd", "gpu", "gpu_cores"]

##remove outlier 
data22 = data22.sort_values("time")
new_data22 = data22[1:]

##create histograms with size 10,10
hist21 = data21.hist(figsize = [10,10], bins = 20)
hist22 = new_data22.hist(figsize = [10,10], bins = 20)