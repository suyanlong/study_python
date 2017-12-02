#! /usr/bin/env python2
# -*- coding:utf-8 -*-


def foo(*args):
    print(args)


def bar(**kvarge):
    print(kvarge)


def foo_bar(*args, **kvarge):
    print(args)
    print(kvarge)


def look(name, year = 12, time = 12):
    print("=====look=====")
    print(name)
    print(year)
    print(time)


def args_kv(*args, **kvarge):
    look(*args, **kvarge)  # 这个地方需要注意了,'*' '**'不要忘掉!!自动解析


# 从运行结果,我们可以看到以 '*' 开头的是
if __name__ == '__main__':
    foo(12, 'sdf', 12323, "dsfdsa")
    # bar(12, 'sdf', 12323, "dsfdsa")  错误
    bar(x = 12, y = 2345, z = '3241')
    foo_bar(123, 13212, 123123, self = 123)
    # look('suyanlong')
    args_kv('suyanlong', 2, 3)
    # args_kv('suyanlong', 2, time1 = 8883) 错误,名字不对
    args_kv('suyanlong', 2, time = 8883)
    args_kv('suyanlong', year = 2312, time = 8883)
    args_kv(name = 'suyanlong1212', year = 2312, time = 8883)
