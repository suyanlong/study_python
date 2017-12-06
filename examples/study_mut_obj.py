#! /usr/bin/env python2
# -*- coding:utf-8 -*-
# Python 的所有变量其实都是指向内存中的对象的一个指针，所有的变量都是！此外，对象还分两类：一类是可修改的，一类是不可修改的。
# 而类型变量分为： 可变对象与不可变对象
# 不可变对象： int,string,float,tuple。即原子类型
# 可变对象： list,dict等。 复合\复杂类型。

def int_test():
    i = 77
    j = 77
    print(id(77))  # 140396579590760
    print('i id:' + str(id(i)))  # i id:140396579590760
    print('j id:' + str(id(j)))  # j id:140396579590760
    print i is j  # True

    j = j + 1
    print('new i id:' + str(id(i)))  # new i id:140396579590760
    print('new j id:' + str(id(j)))  # new j id:140396579590736
    print i is j  # False


if __name__ == '__main__':
    int_test()
