import requests
import json
import streamObject

class checkForLive():
    def __init__(self):
        self.mainPageUrl = "https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/395/F1_TV_Pro_Monthly/14"

    def getResultObj(self):
        try:
            r = requests.get(self.mainPageUrl)
        except:
            print("Failed to check for live.")
            return ""
        return r

    def checkForLive(self):
        raw = self.getResultObj()
        if raw.text == "":
            return False

        jsn = json.loads(raw.text)
        state = jsn['resultObj']['containers'][0]['retrieveItems']['resultObj']['containers'][0]['metadata']['entitlement']
        if state == "Access":
            return False
        else:
            return True