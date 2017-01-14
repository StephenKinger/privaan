import requests
from config import *

class GeoIPInformation():
    def __init__(self):
        self.uri = 'http://freegeoip.net/json/'

    def GetIPInfo(self, ip):
        print 'request' + self.uri + ip
        r = requests.get(self.uri+ip)
        print r.json()
        self.info = r.json()
        return self.formatIPInfo()

    def formatIPInfo(self):
        info = """\
        <table style="border:solid 1px black;">
            <tr style="border:solid 1px black;">
                <td style="border:solid 1px black; text-align: center;">City</td>
                <td style="border:solid 1px black; text-align: center;">region_name</td>
                <td style="border:solid 1px black; text-align: center;">longitude</td>
                <td style="border:solid 1px black; text-align: center;">lattitude</td>
                <td style="border:solid 1px black; text-align: center;">Country name</td>
                <td style="border:solid 1px black; text-align: center;">IP</td>
            </tr>
            <tr>
            """
        info += '<td style="border:solid 1px black; text-align: center;">' + self.info['city'] + '</td>\n'
        info += '<td style="border:solid 1px black; text-align: center;">' + self.info['region_name'] + '</td>\n'
        info += '<td style="border:solid 1px black; text-align: center;">' + str(self.info['longitude']) + '</td>\n'
        info += '<td style="border:solid 1px black; text-align: center;">' + str(self.info['latitude']) + '</td>\n'
        info += '<td style="border:solid 1px black; text-align: center;">' + self.info['country_name'] + '</td>\n'
        info += '<td style="border:solid 1px black; text-align: center;">' + self.info['ip'] + '</td>\n'
        info += '</tr>\n</table>\n'
        if map_box_api_key != '':
            info += "<img width=\"600\" src=\"https://api.mapbox.com/v4/mapbox.emerald/"+str(self.info['longitude'])+","+str(self.info['latitude'])+",10/480x360@2x.png?access_token="+map_box_api_key+"\" alt=\"Mapbox Map of "+str(self.info['longitude'])+","+str(self.info['latitude'])+"\">"
            info += "Copyright <a href='https://www.mapbox.com/map-feedback/'>Mapbox</a> Copyright <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap contributors</a>"
        return info
