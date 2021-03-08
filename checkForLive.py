import requests
import json
import streamObject

class checkForLive():
    def __init__(self):
        self.archiveURL = 'https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/493/F1_TV_Pro_Monthly/2'
        self.baseURL = 'https://f1tv.formula1.com/'

    def getResultObj(self):
        r = requests.get(self.archiveURL)
        return json.loads(r.text)

    def checkForLive(self):
        json = self.getResultObj()

        state = json['resultObj']['containers'][0]['retrieveItems']['resultObj']['containers'][0]['metadata']['emfAttributes']['state']
        if state == "Archive":
            return False
        else:
            return True