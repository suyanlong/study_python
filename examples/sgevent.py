#! /usr/bin/env python2
# -*- coding:utf-8 -*-
import gevent


def foo():
    print "runing in foo"
    gevent.sleep(1)


# python 存在默认参数,

# 可变参数
def bar(*c, **agrs):
    print len(c)

    for x in c:
        print x

    for x in agrs:
        print x + ':' + str(agrs[x])
        # print agrs[1]


if __name__ == '__main__':
    foo()
    print __file__
    print __package__
    print __doc__
    bar(123, 123, 4, 54, 6, 2, k = 3, key1 = 12, key2 = 120)
