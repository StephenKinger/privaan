import privaan.notify
import privaan.config
from mock import patch
import unittest
import privaan.apacheLogListener
import os


class TestApacheLogListener(unittest.TestCase):

    def printer(self, msg):
        if self.count == 0:
            self.assertEqual(msg, 'GRANTED access occured from IP 83.243.102.1')
            self.count += 1
        elif self.count == 1:
            self.assertEqual(msg, 'UNAUTHORIZED access occured from IP 66.249.93.30')
            self.count +=1
        elif self.count == 2:
            self.assertEqual(msg, 'BAD_REQUEST access occured from IP 185.83.161.4')
    
    def test_one_file(self):
        self.count = 0
        path = os.getcwd()
        listener = privaan.apacheLogListener.ApacheLogListener('./access.log')
        
        listener.Watch(self.printer)
        



if __name__ == '__main__':
    unittest.main()