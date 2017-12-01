#! /usr/bin/env python2
# -*- coding:utf-8 -*-


from gevent import monkey

monkey.patch_all()
# monkey.patch_socket()
import gevent

import urllib2


def one():
    def f(n):
        for i in range(n):
            print gevent.getcurrent(), i
            # 当然，实际代码里，我们不会用gevent.sleep()
            # 去切换协程，而是在执行到IO操作时，gevent自动切换，
            gevent.sleep(0)

    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    g1.join()
    g2.join()
    g3.join()


def two():
    def f(url):
        print('GET: %s' % url)
        resp = urllib2.urlopen(url)
        data = resp.read()
        print data
        print('%d bytes received from %s.' % (len(data), url))

    gevent.joinall([
        # gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
    ])


if __name__ == "__main__":
    one()
    two()
