import requests

url = "https://atlas.ripe.net/api/v2/probes/?country_code={}&status=1"
country_codes = [("LB", 5), ("JO", 5), ("SY", 5), ("EG", 5),
                 ("IQ", 5), ("SA", 5), ("BH", 5), ("QA", 5), ("OM", 5)]
probes_per_country = dict()
online_probes = []
for i in country_codes:
    probes_per_country[i[0]] = []
    r = requests.get(url.format(i[0]))
    data = r.json()
    for j in range(min(i[1], len(data["results"]))):
        online_probes.append(data["results"][j]["id"])
        probes_per_country[i[0]].append(data["results"][j]["id"])

print(online_probes, len(online_probes))
print(probes_per_country)
