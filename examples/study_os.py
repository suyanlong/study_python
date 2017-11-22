#! /usr/bin/env python2
# -*- coding:utf-8 -*-


import os
import sys
from pprint import pprint

pprint(os.getcwd())
pprint(sys.argv[0])
pprint(os.path.abspath(sys.argv[0]))
pprint(os.path.curdir)