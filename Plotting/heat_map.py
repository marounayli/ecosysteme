import numpy as np
import mean_pcountry_pIP
import resources
import random
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
Games_IPS = resources.get_games_ips()
Games = ["DOTA2", "LOL", "PUBG", "CSGO"]
MAP = {"DOTA2": dict(), "LOL": dict(), "PUBG": dict(), "CSGO": dict()}
AGGREGATED_DATA = mean_pcountry_pIP.get_1d_aggregation()
countries = AGGREGATED_DATA[random.sample(list(AGGREGATED_DATA), 1)[0]].keys()
for game in Games:
    for country in countries:
        MAP[game][country] = []

for ip in AGGREGATED_DATA:
    game = Games_IPS[ip]
    for country in countries:
        MAP[game][country].append(AGGREGATED_DATA[ip][country])


for game in MAP:
    for country in countries:
        if len(MAP[game][country]) > 0:
            MAP[game][country] = np.median(MAP[game][country])
        else:
            MAP[game][country] = 0

Data =[]
for i in MAP:
    arr=[]
    for j in MAP[i]:
        arr.append(MAP[i][j])
    Data.append(arr) 

df = pd.DataFrame(MAP, columns=MAP.keys())
print(df)
# ax = sb.heatmap(df,annot=True,fmt="f", linewidths=0.5, cmap="inferno")
# plt.show()
