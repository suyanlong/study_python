#! /usr/bin/env python2
# -*- coding:utf-8 -*-

def display2(func):
    func()


def display1(func):
    func()


def option(*param_decls, **attrs):
    pass


def option1(*param_decls, **attrs):
    pass


def command(name = None, cls = None, **attrs):
    def decorator(f):
        pass

    return decorator


# 再次强调，python是解释型语言！！！一步一步的解释。
# @display1()
# 原来这里返回的是一个函数.以及通过可变参数控制的，所以python里面的@语法糖形式：@函数名。
# 执行循序自上而下的先有最底层的函数执行。
@command()
@command()
@command()
@option
def display():
    print 'display() function'


def command(name = None, cls = None, **attrs):
    def decorator(f):
        pass

    return decorator


# ------------------------------------------------------------
def a(fn):
    print 'a'

    def d(st):
        print st + 'd'

    return d


def b(fn):
    print 'b'
    return fn


@a
@b
def c(st):
    print st


c('c1212')
# d('c1212')经过装饰器，函数名字还是原来的名字，但是函数的逻辑已经被替换了。装饰，装饰，装饰，改变它的逻辑！
c('c1212')
c('c1212')
c('c1212')
