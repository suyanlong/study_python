#! /usr/bin/env python2
# -*- coding:utf-8 -*-


from setuptools import setup

setup(
    name = 'hello',
    version = '0.1',
    py_modules = ['hello'],
    install_requires = [
        'Click',
    ],
    entry_points = '''
        [console_scripts]
        hello=hello:cli
    ''',
)

# pip install --editable . 生成命令
# python setup.py sdist  打成tar.gz包
# python setup.py bdist_wheel 打成whl包
# python setup.py sdist bdist_wheel 一起打whl，tar.gz包

# tar.gz 与 whl包之间怎么转化？
# pip wheel leveldb-0.194.tar.gz  => leveldb-0.194-cp27-cp27mu-linux_x86_64.whl
# pip wheel [*.tar.gz] 就可以了转换为whl包了。