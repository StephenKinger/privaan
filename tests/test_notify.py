import privaan.notify
import privaan.config
import mock
from mock import patch
import unittest
from smtplib import SMTP

class TestNotify(unittest.TestCase):

    @patch("smtplib.SMTP")
    def test_one_recipient_refused(self, mock_smtp):
        # Build test message

        # Returns a send failur for the first recipient
        instance = mock_smtp.return_value

        # Call 'send_message' function
        result = privaan.notify.notify('hello')

        mock_smtp.return_value.sendmail.assert_called_once_with(
            privaan.config.fromaddr, privaan.config.toaddrs, mock.ANY)


if __name__ == '__main__':
    unittest.main()
