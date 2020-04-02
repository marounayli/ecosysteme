import requests
import logging_manager
url = "https://atlas.ripe.net/api/v2/probes/?country_code={}&status=1"
country_codes = [("LB", 5), ("JO", 5), ("SY", 5), ("EG", 5),
                 ("IQ", 5), ("SA", 5), ("BH", 5), ("QA", 5), ("OM", 5)]


def dynamic_probe_loading():
    probes_per_country = dict()
    online_probes = []
    logs=[]
    for i in country_codes:
        probes_per_country[i[0]] = []
        r = requests.get(url.format(i[0]))
        data = r.json()
        results=data["results"]
        for j in range(min(i[1], len(results))):
            online_probes.append(str(results[j]["id"]))
            logs.append((str(results[j]["id"]),i[0]))
    logging_manager.logActiveProbes(logs)
    return online_probes
