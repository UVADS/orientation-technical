import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\kimbrelljm17\OneDrive - Grove City College\Documents\UVA\Orientation\2021-06-15-survey.csv")
data.hist()

plt.show()


