import json
import resources
import numpy as np
import os

coutry_probe_map = resources.get_probe_country_map()
results_raw = dict()
results_filtered=dict()
results_path="../Results"
results_files = []
for r, d, f in os.walk(results_path):
    for file in f:
        results_files.append(os.path.join(r, file))

def get_1d_aggregation():
    DATA_AGGREGATION=dict()
    for file in results_files:
        for i in coutry_probe_map.keys():
            results_raw[i] = list()
    
        for i in resources.get_countries():
            results_filtered[i]=[0,0]

        with open(file,'r') as data_set: ## Just add for loop for the all the measurements and store them somewhere
            data=json.load(data_set)
            Destination=data[0]["dst_addr"]
            for i in data:
                if i["avg"] == -1:
                    continue
                results_raw[i["prb_id"]].append(i["avg"])

        for i in results_raw :
            if len(results_raw[i])!=0:
                results_raw[i]=np.median(results_raw[i])

        for i in results_raw:
            results_filtered[coutry_probe_map[i]][0]+=1
            results_filtered[coutry_probe_map[i]][1]+=results_raw[i]
        polluted=[]
        for i in results_filtered:
            if(results_filtered[i][1].size!=0):
                results_filtered[i]=results_filtered[i][1]/results_filtered[i][0]
            else:
                polluted.append(i)
        for i in polluted:
           del results_filtered[i]

        DATA_AGGREGATION[Destination]=results_filtered
    return DATA_AGGREGATION
# print(get_1d_aggregation())