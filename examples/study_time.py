#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import time, datetime, sys

if __name__ == '__main__':
    print time.time()
    print  time.daylight
    print datetime.date(1990, 2, 3)
    # 获取当前时间？
    print time.localtime()
    time.sleep(1)
    print time.timezone
    print time.gmtime()
    print time.localtime()
    print time.mktime(time.localtime())
    print time.strftime("%Y-%m-%d %X", time.localtime())
    print sys.platform
    print sys.path
