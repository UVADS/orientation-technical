# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
#import matplotlib
import numpy as np
import matplotlib.pyplot as plt

data22 = pd.read_csv("https://github.com/UVADS/orientation-technical/blob/main/dat/2022-06-14-survey.csv")

#CPU_hist = data22['CPU_cores'].hist(bins = 15, grid= False)
#CPU_hist.set_xlabel("CPU Cores")
#CPU_hist.set_ylabel("Count")

plt.hist(data22['CPU_cores'], bins=range(0,16), color="indigo", align="left")
plt.xlabel("CPU Cores")
plt.ylabel("Num Machines")
plt.title("MSDS '23 CPU Cores")
plt.xticks(np.arange(0,16,2)) #cuts off -3; not valid value
plt.yticks(range(0,19,2))

data22['RAM'] = data22['RAM'].astype('category') # Not a continuous thing
plt.bar(data22['RAM'], color = "darkcyan")
plt.xlabel("RAM")
plt.ylabel("Num Machines")
plt.title("MSDS '23 RAM")