# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dat = pd.read_csv("https://github.com/UVADS/orientation-technical/raw/main/dat/2022-06-14-survey.csv")

plt.hist(dat["RAM (in GB)"], bins=9,range=(0,36), edgecolor="black")
plt.xticks(ticks=np.arange(0,40,4))
plt.xlabel("RAM (in GB)")
plt.ylabel("Count")
plt.title("HistogRAM")