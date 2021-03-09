import requests
import json
#import selenium

class authenticate:
    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd
        self.ascendontoken = ""
        self.entitlementToken = ""
        self.loggedIn = False
        self.authUrl = "https://api.formula1.com/v2/account/subscriber/authenticate/by-password"
        self.apikey = 'fCUCjWrKPu9ylJwRAv8BpGLEgiAuThx7'

    # First, poll auth/by-password with apiKey and user,pass
    def authenticate(self):
        headers = {'apikey': self.apikey, 'Login': self.user, 'Password': self.passwd, 'content-type': 'application/json', 'accept': 'application/json, text/javascript, */*; q=0.01', 'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36', 'cookie': 'talkative_qos_bandwidth=3.47; euconsent-v2=CPCrv0LPCrv0LAvACDENBQCgAAAAAAAAAAAAAAAAAAAA.YAAAAAAAAAAA; notice_preferences=0:; TAconsentID=c93bbf73-0fb3-46d4-9b76-f3b020e816c7; notice_gdpr_prefs=0::implied,eu; cmapi_gtm_bl=ga-ms-ua-ta-asp-bzi-sp-awct-cts-csm-img-flc-fls-mpm-mpr-m6d-tc-tdc; cmapi_cookie_privacy=permit 1 required; notice_behavior=implied,eu; _gid=GA1.2.2092720539.1615115103; user-metadata=%7B%22subscriptionSource%22%3A%22%22%2C%22userRegistrationLevel%22%3A%22full%22%2C%22subscribedProduct%22%3A%22F1%20TV%20Pro%20Monthly%22%2C%22subscriptionExpiry%22%3A%2299%2F99%2F9999%22%7D; isFirstRendering=true; _ga_D9BP6Y3R6M=GS1.1.1615197457.9.1.1615198207.0; _ga=GA1.2.873412065.1615114980; _gat_F1GAlegacy=1; reese84=3:EQVNbeuAGAs48uSHoi++0g==:IEmYjJ40i3MOmJdA9JD6vYDsYg45vAOkcYcbP3J5mmhFjFwmZCdQHzE+NvoB5Oy9Y7E6jpkDxCF7jhqJX24ilmiSESzfU24PA38Q3gWGh61/ZbRWZaIGI2u1kYWkIEJJ+oRHyrAl/+OQmQr3fPsHZbN3BS+tK/8XayGZDaOEksCPMx3FG3XNCe2pvtgwCEQ+rqrnGSGsRipeALSl2mreUYwcTAx6VMm+bKu30iYj4NfiyRK2b3VckdYAd7UpSKbkEs20Wlps1Hjut6OuC7JCtHRByUCmirjAQ0Z1dkF3YP/cs3F9UILbUyjaR80EYSNjg4QsUESuvL14BV4BDR+nN8RGriMgUr3lQs54S1qFYujC/reVZcCb3GoBSzx8EfYImmQIo8x1b8jCSlbzFlvUu9Rsx8Irg1I1pP8GZgPHfSyb2TMVRxaymmxSBaVB7khb:x7T2YsxSMHdLy8XtqKLVycd5zkaLCbDgnEEANM4O7Eo=; talkative_customer_journey_initial_time=1615198210347'}
        params = {'Login': self.user, 'Password': self.passwd}
        r = requests.post(self.authUrl, params=headers, headers=headers)
        #print(r.status_code)
        #print(r.text)
        # Authenticate and store token

    def getEntitlementToken(self):
        return self.entitlementToken

    def logout(self):
        self.user = ""
        self.passwd = ""
        self.ascendontoken = ""
        self.entitlementToken = ""
        self.loggedIn = False

    def authByEntitlementToken(self):
        #x = open("./entitlement.json", 'w+')
        #x.close()
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