import requests
import json
import streamObject
import time

url = "/CONTENT/PLAY?channelId=1018&contentId=1000000807"

archiveURL = 'https://f1tv.formula1.com/2.0/R/ENG/WEB_DASH/ALL/PAGE/493/F1_TV_Pro_Monthly/2'
baseURL = 'https://f1tv.formula1.com'
basePlayUrl = 'https://f1tv.formula1.com1.0/R/ENG/WEB_HLS/ALL'
targetURL = baseURL + url

u = 'https://f1tv.formula1.com/1.0/R/ENG/WEB_HLS/ALL/CONTENT/PLAY?contentId=1000000807'
params = {'ascendontoken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJFeHRlcm5hbEF1dGhvcml6YXRpb25zQ29udGV4dERhdGEiOiJVU0EiLCJTdWJzY3JpcHRpb25TdGF0dXMiOiJhY3RpdmUiLCJTdWJzY3JpYmVySWQiOiIxNTQzNzg3MzgiLCJGaXJzdE5hbWUiOiJGZWxpeCIsIkxhc3ROYW1lIjoiS3J1ZWxscyIsImV4cCI6MTYxNjMyNDgxNSwiU2Vzc2lvbklkIjoiZXlKaGJHY2lPaUpvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBeEx6QTBMM2h0YkdSemFXY3RiVzl5WlNOb2JXRmpMWE5vWVRJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmlkU0k2SWpFd01ERXhJaXdpYzJraU9pSTJNR0U1WVdRNE5DMWxPVE5rTFRRNE1HWXRPREJrTmkxaFpqTTNORGswWmpKbE1qSWlMQ0pvZEhSd09pOHZjMk5vWlcxaGN5NTRiV3h6YjJGd0xtOXlaeTkzY3k4eU1EQTFMekExTDJsa1pXNTBhWFI1TDJOc1lXbHRjeTl1WVcxbGFXUmxiblJwWm1sbGNpSTZJakUxTkRNM09EY3pPQ0lzSW1sa0lqb2lNMlkxTWpFeE5qRXRZbU00TWkwME1UUTJMV0ZsTVRZdE0yUXpNekl3WVRsbVpUUm1JaXdpZENJNklqRWlMQ0prWXlJNklqTTJORFFpTENKc0lqb2laR1V0UkVVaUxDSmtkQ0k2SWpFaUxDSmxaQ0k2SWpBMEx6QTJMekl3TWpFZ01URTZNRFk2TlRVaUxDSmhaV1FpT2lJd015OHlNUzh5TURJeElERXhPakEyT2pVMUlpd2lZMlZrSWpvaU1ETXZNRGd2TWpBeU1TQXhNVG93TmpvMU5TSXNJbWx3SWpvaU1qQXdNVG8wWkdRM09qRTRNemc2TURveU1UaGhPalUxTkdRNk9USTNOVG8zWmpnNElpd2lZeUk2SWt0UFJVeE9MVlpQUjBWTVUwRk9SeUlzSW5Caklqb2lOVEE0TWpraUxDSmpieUk2SWtSRlZTSXNJbXhoZENJNklqVXdMamsxT0RjaUxDSnNiMjVuSWpvaU5pNDROems1SWl3aWJtSm1Jam94TmpFMU1URTFNakUxTENKbGVIQWlPakUyTVRjM01EY3lNVFVzSW1semN5STZJbUZ6WTJWdVpHOXVMblIySWl3aVlYVmtJam9pWVhOalpXNWtiMjR1ZEhZaWZRLlpmTlpDYXAzbEdQZEJ0YUxZTHdMM2RYUDN1VTFWcUZJQjFJU1J5YnV1QTgiLCJpYXQiOjE2MTUxMTUyMTUsIlN1YnNjcmliZWRQcm9kdWN0IjoiRjEgVFYgUHJvIE1vbnRobHkiLCJqdGkiOiI4OWNkZjFlOC1iNGQ3LTRjYjgtYmMxYS00M2ZiZTViMzdjNGEifQ.HbDBuGVRki-4EoiOR0Y4LWeOscugJn6Puwm_hJkxdXYPk-DVa-9b9SCms9P3ZwqxpnyQqTNpxw7S8yJsjmdiqjUSQTgeRyuRuoOhjTLwQDia_KQthOp8uemZuUySZxf4qWVpypxWsvP5kkamGJm0S3VnY8M7mLfXCWCnbZ30e5qloEXx9zc_7klISpj8wJ0Ix4_zESmYibrWF1XLd8nxdDvV2TVvv4bJOvaH7WHceN81_6gxs43ldumjUfe1CTnAiUw-ZLw8z9ar45B5duzWotFkHi4_ftOThjBMCPQeWVaDkEN2gGH8RemCLGnf8J7JiqNy44GAME57u4AjimvjMg'}

#r = requests.get(u, headers=params)

#print(r.text)

class getTokenizedUrl:
    def __init__(self, url, authObj):
        self.basePlayUrl = 'https://f1tv.formula1.com/1.0/R/ENG/WEB_HLS/ALL/'
        self.url = self.basePlayUrl + url
        self.authObj = authObj
        #print("Init")

    def getUrl(self):
        #print(self.url)
        token = self.authObj.getEntitlementToken()
        params = {'entitlementtoken': token}
        r = requests.get(self.url, headers=params)
        jso = json.loads(r.text)
        #print(jso)
        url = jso['resultObj']['url']
        #print(url)
        #time.sleep(15)
        return url