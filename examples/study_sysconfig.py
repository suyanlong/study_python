#! /usr/bin/env python2
# -*- coding:utf-8 -*-


import sysconfig
from pprint import pprint

pprint(sysconfig.get_path_names())

pprint(sysconfig.get_python_version())

pprint(sysconfig.get_config_h_filename())

pprint(sysconfig.get_platform())

pprint(sysconfig.get_makefile_filename())

# pprint(sysconfig.get_config_h_filename())

# pprint(sysconfig.get())
