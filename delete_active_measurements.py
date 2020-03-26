import requests
import config
to_be_stopped=[]
for i in range(1,20):
    r = requests.get("https://atlas.ripe.net/api/v2/measurements/my/?key="+config.API_KEY_Maroun+"&page="+str(i))
    data = r.json()["results"]

    for item in data :
        print(item["status"]["name"])
        if(item["status"]["name"]!="Stopped"):
            to_be_stopped.append(item["id"])


for id in to_be_stopped:
    r = requests.delete("https://atlas.ripe.net/api/v2/measurements/"+str(id)+"/?key="+config.API_KEY_Maroun)
    if(r.ok):
        print("Measurement", str(id) , "was successfully stopped")
    else:
        print("There was a problem stopping measurement",id)

