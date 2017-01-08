import privaan.notify
import privaan.config
from mock import patch
import unittest
import privaan.apacheLogListener
import os


class TestApacheLogListener(unittest.TestCase):

    def printer(self, msg):
       self.assertEqual(msg, 'GRANTED access occured from IP 83.243.102.1\nUNAUTHORIZED access occured from IP 66.249.93.30\nBAD_REQUEST access occured from IP 185.83.161.4\n')
    
    def test_one_file(self):
        self.count = 0
        path = os.getcwd()
        listener = privaan.apacheLogListener.ApacheLogListener('./access.log')
        
        listener.Check(self.printer)
        



if __name__ == '__main__':
    unittest.main()