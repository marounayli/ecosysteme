import requests
import json

baseURL = "https://atlas.ripe.net/api/v2/measurements/?key="
API_KEY_Maroun = "79a48bbe-42d3-4ed2-893f-bae997321d2e"

files=["DOTA2","PUBG","LOL"]
Games = dict()
for file in files:
    with open(file+".txt" , 'r') as f:
        data=[]
        for line in f:
            data.append(line.rstrip().split('-'))
        Games[file]=data

for k, v in Games.items():
    for ip in v:
        data= {
            "definitions": [
                {
                    "target": str(ip[0]),
                    "description": "Ping to the server " + str(ip[1]) + " " + str(k),
                    "type": "ping",
                    "af": 4,
                    "is_oneoff" : True
                }
            ],
            "probes": [
                {
                    "requested": 18,
                    "type": "probes",
                    "value": "3474, 4452, 51488, 35734, 51863, 34151, 16687, 17775, 2949, 30120, 50764, 30783, 29599, 50834, 6090, 25901, 1000245, 31132"
                }
            ]
        }
        
        url = baseURL + API_KEY_Maroun
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)

        print(r.content)
        
