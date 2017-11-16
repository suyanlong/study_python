#! /usr/bin/env python2
# -*- coding:utf-8 -*-

# 初学者必知的Python中优雅的用法
from __future__ import division
import pprint
import pdb

# 1.
list = {1, 2, 3, 4, 5, 6, 7, 8, 9}

for i, item in enumerate(list):
    print i, item

# 2.

my_dict = {i: i * i for i in xrange(100)}
my_set = {i * 15 for i in xrange(100)}

pprint.pprint(my_dict)
pprint.pprint(my_set)

# 3. 引入__futrue__特性，需要放到文件头部地方。
# from __future__ import division
pprint.pprint(1 / 2)

# 4. 快速开启HTTP服务,共享自己的资源，让别的机器访问你的设置被访问的资源。
# Python2
# python -m SimpleHTTPServer

# Python 3
# python3 -m http.server

# 5. Python表达式求值
expr = "[1, 2, 3]"
my_list = eval(expr)
print my_list

# 6. python脚本分析
# python - m cProfile my_script.py

# 7. 对象自检,dir()会返回对象的属性名字。
foo = [1, 2, 3, 4]
print dir(foo)

# 8. if的结构化
n = 4
if n in [1, 4, 5, 6]:
    print n

# 9. 字符串/数列 逆序
a = [1, 2, 3, 4]
print a[::-1]

# 三元运算符
# [on_true] if [expression] else [on_false]
x, y = 50, 25
small = x if x < y else y


