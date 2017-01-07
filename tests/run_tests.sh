#!/bin/bash
export PYTHONPATH=`pwd`/..:$PYTHONPATH
rm *.offset
python -m unittest discover
rm *.offset