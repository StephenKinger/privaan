#!/bin/bash
export PYTHONPATH=`pwd`/..:$PYTHONPATH
if [ -f access.txt.offset ]
  then rm *.offset
fi
python -m unittest discover
