# %%
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datasets/2022-06-14-survey.csv")
df
# %%
for i in range(len(df.columns)):

    fig, ax = plt.subplots()
    ax.set_title(df.columns[i])
    ax.hist(df[df.columns[i]])
# %% 
df
# %%
df = df.sort_values("GPU CUDA Number of Cores (int)",ascending=False)
df
# %% 
new_df = df[1:]
new_df
for i in range(len(df.columns)):

    fig, ax = plt.subplots()
    ax.set_title(new_df.columns[i])
    ax.hist(new_df[new_df.columns[i]])
# %% 
new_df.hist()
