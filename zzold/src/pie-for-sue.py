# Pete Alonzi (lpa2a@virginia.edu)
# A script to make a pie chart of student laptops for the IT Director
# 2021-06-15
# Evidence to support the need for CEDS

# imports and figure setup
import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, aspect=1)

# read in data
df = pd.read_csv('../data/survey.csv')

# calculate counts for OS
myPlot = df.groupby(['Operating System']).size().plot.pie(y='Operating System', figsize=(10,10),colormap='Accent',autopct='%.1i') 

# make the plot
ax.set_title("MSDS Student Operating System", fontsize=20, verticalalignment='bottom')
ax.set(ylabel=None)

# show the plot
plt.show()
