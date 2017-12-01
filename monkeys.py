#! /usr/bin/env python2
# -*- coding:utf-8 -*-


import socket

print(socket.socket)

print("Aftermonkey patch")
from gevent import monkey

monkey.patch_socket()
print(socket.socket)

import select

print(select.select)
monkey.patch_select()
print("Aftermonkey patch")
print(select.select)
