import requests

class GeoIPInformation():
    def __init__(self):
        self.uri = 'http://freegeoip.net/json/'
        
    def GetIPInfo(self, ip):
        print 'request' + self.uri + ip
        r = requests.get(self.uri+ip)
        print r
        print r.json()
        print r.json()['time_zone']
        