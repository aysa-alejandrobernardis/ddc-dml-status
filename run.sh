#!/bin/bash
export PYTHONPATH=${PYTHONPATH}:/Volumes/Projects/library/python2.7/dev/lib/python2.7/site-packages:/Volumes/Projects/library/python2.7/flask/lib/python2.7/site-packages
export DATABASE_URL="postgresql://bernardisa@localhost/bernardisa"
python2.7 -m app