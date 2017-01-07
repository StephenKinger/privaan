"""privaan tool to be notifyed when someone access to an apache server.

Usage: __init__.py LOGFILE

Arguments:
    LOGFILE  path to the log file

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
import privaan.notify
import privaan.apacheLogListener


if __name__ == '__main__':
    arguments = docopt(__doc__, version='privaan 0.0.1')
    listener = privaan.apacheLogListener.ApacheLogListener(arguments['LOGFILE'])
    listener.Watch(privaan.notify.notify)