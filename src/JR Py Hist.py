import matplotlib
import pandas

#create Dataframe from CSV File
df = pandas.read_csv (r'https://raw.githubusercontent.com/UVADS/orientation-technical/main/dat/2022-06-14-survey.csv')

df = df.sort_values('Timestamp', ignore_index=True)
print(df)
df = df.drop(0)

import matplotlib.pyplot as plt


plt.hist(df['CPU Number of Cores (int)'])
plt.title('Distribution of CPU Core Count')
plt.xlabel('Number of Cores')
plt.ylabel('Frequency')
plt.show()