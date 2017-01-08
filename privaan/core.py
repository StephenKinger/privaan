"""privaan tool to be notifyed when someone access to an apache server.

Usage: __init__.py LOGFILE

Arguments:
    LOGFILE  path to the log file

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
from apacheLogListener import ApacheLogListener
from notify import notify

__all__ = ['privaan_run', '__version__']

__version__ = "0.0.1"

def privaan_run():
    args = docopt(__doc__, version=__version__)
    listener = ApacheLogListener(args['LOGFILE'])
    listener.Watch(notify)
    

if __name__ == '__main__':
    privaan_run()