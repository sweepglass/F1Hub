import requests
import json
#import selenium

class authenticate:
    def __init__(self, user, passwd):
        self.sessionId = ""
        self.user = user
        self.passwd = passwd
        self.ascendontoken = ""
        self.entitlementToken = ""
        self.loggedIn = False
        self.authUrl = "https://api.formula1.com/v2/account/subscriber/authenticate/by-password"
        self.entitlementUrl = "https://f1tv.formula1.com/1.0/R/ENG/WEB_DASH/ALL/USER/ENTITLEMENT"
        self.apikey = 'fCUCjWrKPu9ylJwRAv8BpGLEgiAuThx7'
        self.distribution = 'd861e38f-05ea-4063-8776-a7e2b6d885a4'
        if self.user == "" or self.passwd == "":
            if self.loginFileExists():
                try:
                    f = open('./login.json', 'r')
                    jsn = json.loads(f.read())
                    self.user = jsn['login']
                    self.passwd = jsn['password']
                    f.close()
                    self.authenticate()
                except:
                    pass

        else:
            if not self.loginFileExists():
                try:
                    f = open('./login.json', 'w+')
                    f.write('{"login":"' + self.user + '","password":"' + self.passwd + '"}')
                    f.close()
                except:
                    pass


    # First, poll auth/by-password with apiKey and user,pass
    def authenticate(self):
        try:
            
            headers = {"apikey":"fCUCjWrKPu9ylJwRAv8BpGLEgiAuThx7", "content-type":"application/json", "cookie":"reese84="}
            data = '{"Login":"'+self.user+'", "Password":"'+self.passwd+'"}'
            r = requests.post(self.authUrl, data=data, headers=headers)
            if not r.status_code == 200:
                raise Exception("Wrong username or password")

            # Authenticate and store token
            jsn = json.loads(r.text)
            self.sessionId = jsn['data']['subscriptionToken']

            headers = {"apikey":"fCUCjWrKPu9ylJwRAv8BpGLEgiAuThx7", "content-type":"application/json", "cookie":"reese84=", "ascendontoken":self.sessionId}
            e = requests.get(self.entitlementUrl, headers=headers)
            if not e.status_code == 200:
                raise Exception("Couldn't get Entitlement Token")
            jsn = json.loads(e.text)
            self.entitlementToken = jsn['resultObj']['entitlementToken']
        except:
            raise Exception("Failed to authenticate")


    def getEntitlementToken(self):
        return self.entitlementToken

    def logout(self):
        self.user = ""
        self.passwd = ""
        self.ascendontoken = ""
        self.entitlementToken = ""
        self.loggedIn = False

    def authByEntitlementToken(self):
        f = open("./entitlement.json", 'r+')
        tokResponse = f.read()
        tokjson = json.loads(tokResponse)
        token = tokjson['resultObj']['entitlementToken']
        self.entitlementToken = token
        f.close()

    def setUser(self, newUser):
        self.user = newUser

    def setPass(self, newPass):
        self.passwd = newPass

    def printUser(self):
        print(self.user)

    def printPass(self):
        print(self.passwd)

    def loginFileExists(self):
        try:
            f = open('./login.json', 'r')
            f.close
            return True
        except:
            return False