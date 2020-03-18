import requests
import json
import config
import probes

baseURL = "https://atlas.ripe.net/api/v2/measurements/?key="
files = ["DOTA2", "PUBG", "LOL", "CSGO"]
Games = dict()
for file in files:
    with open(file+".txt", 'r') as f:
        data = []
        for line in f:
            data.append(line.rstrip().split('-'))
        Games[file] = data

# preparing the probes:
loaded_probes = probes.dynamic_probe_loading()

for k, v in Games.items():
    for ip in v:
        data = {
            "definitions": [
                {
                    "target": str(ip[0]),
                    "description": "Ping to the server " + str(ip[1]) + " " + str(k),
                    "type": "ping",
                    "af": 4,
                    "is_oneoff": True
                }
            ],
            "probes": [
                {
                    "requested": len(loaded_probes),
                    "type": "probes",
                    "value": (", ").join(loaded_probes)
                }
            ]
        }

        url = baseURL + config.API_KEY_Maroun
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

        print(r.content)
