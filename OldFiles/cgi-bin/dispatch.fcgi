#!/home/jdbigham/jdbigham.com/cgi-bin/testFlask/bin/python

import sys
import os

sys.path.insert(0, '/jdbigham/jdbigham.com/cgi-bin/testFlask/lib/python2.7/site-packages')

from wsgiref.handlers import CGIHandler
from app import app

CGIHandler().run(app)

