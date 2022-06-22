import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv")

# get rid of all spaces in df column names
df.columns = [c.replace(' ', '_') for c in df.columns]
df.columns = [c.replace('(', '') for c in df.columns]
df.columns = [c.replace(')', '') for c in df.columns]

# drop second row
df = df.drop(labels=1, axis=0)

cpu_hist = plt.hist(df.iloc[:,2], bins=6, color="indigo")
plt.title("Histogram of CPU Cycle Rate")
plt.xlabel("CPU Cycle Rate (in GHz)")
plt.ylabel("Frequency")
plt.show()