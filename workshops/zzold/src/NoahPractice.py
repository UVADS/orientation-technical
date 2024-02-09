import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv("https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv")

# used for getting rid of outliers: https://www.askpython.com/python/examples/detection-removal-outliers-in-python
for x in ['CPU Cycle Rate (in GHz)']:
    q75, q25 = np.percentile(data.loc[:, x], [75, 25])
    range = q75 - q25
    max = q75 + (1.5 * range)
    min = q25 - (1.5 * range)
    data.loc[data[x] < min, x] = np.nan
    data.loc[data[x] > max, x] = np.nan

data.hist(column='CPU Cycle Rate (in GHz)', figsize=(6,4))
plt.xlabel('CPU Speed')
plt.ylabel('Number of Computers')
plt.title("How fast are people's CPUs?")
#plt.xscale('log')
plt.show(block=True)