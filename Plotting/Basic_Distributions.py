import json

files=["../dummy.json","../dummy.json"]
Results=[]
counter = dict()
aggregation = dict()
for _file in files:
    with open(_file) as f:
        data = json.load(f)
        Destination=data[0]["dst_addr"]
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
    Results.append((Destination,aggregation))

print(Results)
