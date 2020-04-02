import requests
import json
import config
import probes
import logging_manager
import os
errors = []
successes = []
baseURL = "https://atlas.ripe.net/api/v2/measurements/?key="
path="./IPV4_ADDR"
files = []
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))
Games = dict()
for file in files:
    with open(file, 'r') as f:
        data = []
        for line in f:
            data.append(line.rstrip().split('-'))
            s=os.path.basename(file)
        Games[s[0:len(s)-4]] = data

# preparing the probes:
loaded_probes = probes.dynamic_probe_loading()
print("Loaded probes : " , loaded_probes)
counter=0
for k, v in Games.items():
    for ip in v:
        counter+=1
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
        if(r.ok == False):
            errors.append((ip,k))
            print(r.text)
        else:
            s=r.content.decode("utf-8")
            successes.append((ip[0],s[1:len(s)-1],k))
            print("Success=", s[1:len(s)-1])
        if counter==4:
            break
    break
logging_manager.logerrors(errors)
logging_manager.logsuccesses(successes)