import numpy as np
import mean_pcountry_pIP
import resources
import random

Games_IPS = resources.get_games_ips()
Games = ["DOTA2", "LOL", "PUBG", "CSGO"]
MAP = {"DOTA2": dict(), "LOL": dict(), "PUBG": dict(), "CSGO": dict()}
AGGREGATED_DATA = mean_pcountry_pIP.get_1d_aggregation()
countries = AGGREGATED_DATA[random.sample(list(AGGREGATED_DATA), 1)[0]].keys()
# print(len(Games_IPS))
# print(Games_IPS)
# print(len(AGGREGATED_DATA))
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

print(MAP)
