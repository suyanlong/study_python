#! /usr/bin/env python2
# -*- coding:utf-8 -*-


import random

import gevent


def task(pid):
    """"
    task
    """
    gevent.sleep(random.randint(1, 2))
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)


print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
