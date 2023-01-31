import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests

def get_nba_data():
    # Source: http://www.balldontlie.io/#get-all-players
    api_url = 'https://www.balldontlie.io/api/v1/players'
    params = {
        'per_page': 100
    }
    x = requests.get(api_url, params = params).json()
    return x

nba_player_data = get_nba_data()['data']
nba_df = pd.DataFrame(nba_player_data)

plt.hist(nba_df['height_feet'], density=True, bins=2)  # density=False would make counts
plt.show(block = True)