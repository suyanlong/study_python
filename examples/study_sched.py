#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import sched, time

s = sched.scheduler(time.time, time.sleep)


def print_time():
    print "From print_time", time.time()


def print_some_times():
    print  time.time()
    s.enter(2, 10, print_time, ())
    s.run()
    print print_time()


print_some_times()
