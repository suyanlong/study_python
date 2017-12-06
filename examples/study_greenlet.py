#! /usr/bin/env python2
# -*- coding:utf-8 -*-
# import greenlet
# from greenlet import greenlet

# greenlet的学习笔记
# http://python.jobbole.com/88125/
# def test1():
#     print(12)
#     gr2.switch()
#     print(dir(gr2.getcurrent()))
#     if gr1 == greenlet.getcurrent():
#         print("相等")
#     print(34)
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()
# switch not call: 切换不是调用
# ----------------------------------------------------------------
# import greenlet
#
#
# def test1(x, y):
#     print id(greenlet.getcurrent()), id(greenlet.getcurrent().parent)  # 40240272 40239952
#     z = gr2.switch(x + y)
#     print 'back z', z  # 没有执行
#
#
# def test2(u):
#     print id(greenlet.getcurrent()), id(greenlet.getcurrent().parent)  # 40240352 40239952
#     return 'hehe'
#
#
# gr1 = greenlet.greenlet(test1)
# gr2 = greenlet.greenlet(test2)
# print id(greenlet.getcurrent()), id(gr1), id(gr2)  # 40239952, 40240272, 40240352
# print gr1.switch("hello", " world"), 'back to main'  # hehe back to main
#
#
# import greenlet
#
#
# def test1(x, y):
#     try:
#         z = gr2.switch(x + y)
#     except Exception:
#         print 'catch Exception in test1'
#
#
# def test2(u):
#     assert False
#
#
# gr1 = greenlet.greenlet(test1)
# gr2 = greenlet.greenlet(test2)
# try:
#     gr1.switch("hello", " world")
# except:
#     print 'catch Exception in main'
# ---------------------------------------------------------------
