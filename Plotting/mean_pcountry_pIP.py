import json
import resources
import numpy as np
import os

coutry_probe_map = resources.get_probe_country_map()
results_raw = dict()
results_filtered = dict()
results_path = "../Results"
results_files = []
for r, d, f in os.walk(results_path):
    for file in f:
        results_files.append(os.path.join(r, file))

# print(results_files)
DATA_AGGREGATION = dict()
def get_1d_aggregation():
    counter =0
    for file in results_files:
        counter+=1
        for i in coutry_probe_map.keys():
            results_raw[i] = list()

        for i in resources.get_countries():
            results_filtered[i] = [0, 0]

        # Just add for loop for the all the measurements and store them somewhere
        with open(file, 'r') as data_set:
            data = json.load(data_set)
            Destination = data[0]["dst_addr"]
            for i in data:
                if i["avg"] == -1:
                    continue
                results_raw[i["prb_id"]].append(i["avg"])

        for i in results_raw:
            if len(results_raw[i]) != 0:
                results_raw[i] = np.median(results_raw[i])
            else:
                results_raw[i] = -1
        for i in results_raw:
            if results_filtered[coutry_probe_map[i]][1] == -1:
                continue
            results_filtered[coutry_probe_map[i]][0] += 1
            results_filtered[coutry_probe_map[i]][1] += results_raw[i]
        polluted = []
        for i in results_filtered:
            try:
                results_filtered[i] = results_filtered[i][1] / results_filtered[i][0]
            except:
                polluted.append(i)
        for i in polluted:
            del results_filtered[i]
        # print(results_filtered,Destination)
        DATA_AGGREGATION[Destination]=results_filtered.copy()
    return DATA_AGGREGATION

a=get_1d_aggregation()
print(a)