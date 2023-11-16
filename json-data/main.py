import json
import requests
from datetime import datetime


url = "https://publicapi.traffy.in.th/share/teamchadchart/search"

query = {'offset':'180000'}

payload={}
headers = {}


for index in range(0,185000,950):
    # record start time
    start = datetime.now()

    query['offset']=str(index)
    response = requests.request("GET", url, headers=headers, data=payload, params=query)
    r_string = str(index)
    print("offset: "+r_string+" response: "+str(response.status_code))

    filename = "traffy{offset}.json".format(offset = r_string)

    # Writing to sample.json
    with open(filename, "w") as outfile:
        json_object = json.dumps(response.json(), indent=4)
        outfile.write(json_object)

    # record end time
    end = datetime.now()
    # print elapsed time in seconds
    print("Elapsed time using process_time()", (end - start).total_seconds(), "s")
