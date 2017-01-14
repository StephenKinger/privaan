from pygtail import Pygtail
from datetime import datetime
from datetime import timedelta
import time
from geoip import GeoIPInformation

__all__ = ['ApacheLogListener']


class AccessEntry():
    def __init__(self, record):
        self.ip = record[0]
        self.user = record[2]
        self.date = record[3]
        self.request = record[5] + record[6] + record[7]
        self.status_code = record[8]
        self.size = record[9]

    def isGranted(self):
        return self.status_code == '200'

    def isUnauthorized(self):
        return self.status_code == '401'

    def isBadRequest(self):
        return self.status_code == '400'

    def getIp(self):
        return self.ip

    def getDate(self):
        return datetime.strptime(self.date, "[%d/%b/%Y:%H:%M:%S")

    def getRequest(self):
        return self.request

class ApacheLogListener():

    def __init__(self, logfile):
        self.logfile=logfile

    def Watch(self, callback):
        self.first_run = 1
        while 1:
            self.Check(callback)
            time.sleep(15)
            print "relances"

    def Check(self, callback):
        if self.first_run:
            self.startdate = datetime.now()
            self.first_run = 0
        msg = """\
        <html>
          <head></head>
          <body>
        """
        is_something_to_send = 0
        for line in Pygtail(self.logfile):
            access_entry = AccessEntry(line.split(' '))
            #check if its an old entry
            if self.startdate < access_entry.getDate():
                is_something_to_send = 1
                access_type = 'UNKNOWN'
                if access_entry.isGranted():
                    access_type = 'GRANTED'
                if access_entry.isBadRequest():
                    access_type = 'BAD_REQUEST'
                if access_entry.isUnauthorized():
                    access_type = 'UNAUTHORIZED'
                msg += '<p>'+access_type + ' access occured from IP ' + access_entry.getIp() + '</p>\n'
                msg += '<p>Request '+access_entry.getRequest()+'</p>\n'
                geo = GeoIPInformation()
                msg += geo.GetIPInfo(access_entry.getIp())
            else:
                print "old enty"
                print access_entry
        msg += """\
          </body>
        </html>
        """
        if is_something_to_send:
            callback(msg)
