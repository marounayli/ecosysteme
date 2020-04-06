import requests
import json
import config
measurements = []
measurements_file = open("log_creation_successes.txt", "r")
for line in measurements_file.readlines():
    measurement = line.rstrip().split("##")[2]
    measurements.append(measurement)

for id in measurements:
    url = "https://atlas.ripe.net/api/v2/measurements/%s/results/?key=%s" % (
        id, config.API_KEY_Maroun)
    print(url)
    response = requests.get(url)
    results = json.loads(response.content)
    with open('RESULTS/%s.json' % id, 'w') as json_file:  # to store them as json files
        json.dump(results, json_file, indent=1)

print(measurements)
