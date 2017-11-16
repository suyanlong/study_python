#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import sys
import hashlib

print sys.version_info

if sys.version_info < (3,6):
    import sha3

s = hashlib.sha3_512()
# print s.name
s.update(b"011111")
print s.hexdigest()

# print hashlib.sha256("132")
