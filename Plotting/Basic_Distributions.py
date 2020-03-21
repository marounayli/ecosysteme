import matplotlib.pyplot as plt
import json
counter = dict()
aggregation = dict()
with open('../dummy.json') as f:
    data = json.load(f)
    for i in data:
        if i["avg"] == -1:
            continue
        if i["prb_id"] in aggregation.keys():
            aggregation[i["prb_id"]] += i["avg"]
            counter[i["prb_id"]] += 1
        else:
            aggregation[i["prb_id"]] = i["avg"]
            counter[i["prb_id"]] = 1

for i in aggregation.keys():
    aggregation[i] = aggregation[i]/counter[i]
print(aggregation)
