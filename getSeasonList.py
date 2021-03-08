import requests
from dataclasses import dataclass
import json

@dataclass
class f1tv:
    baseApi: str
    archive: str
    #class miscIDs:
    #    archive: int
    #class seasonIds:
    #    20: str
    #    2019: str
    #    2018: str

f1tv.archive = "https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/493/F1_TV_Pro_Monthly/2"
f1tv.baseApi = "https://f1tv.formula1.com"

r = requests.get(f1tv.archive)
#print(r.status_code)
#print(r.text)


    jsonized = json.loads(r.text)
    objList = jsonized['resultObj']['containers'][2]['retrieveItems']['resultObj']['containers'][0]['metadata']['longDescription']
    objLink = jsonized['resultObj']['containers'][2]['retrieveItems']['resultObj']['containers'][0]['actions'][0]['uri']
    #print(objList, objLink)
#jsonifiedList = []

#for x in range(len(objList)):
#    jsonifiedList.append(json.loads(objList[x]))


