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
# python setup.py sdist bdist_wheel -w ./package


# tar.gz 与 whl包之间怎么转化？
# pip wheel [*.tar.gz] 就可以了转换为whl包了。
# pip wheel leveldb-0.194.tar.gz  => leveldb-0.194-cp27-cp27mu-linux_x86_64.whl

# pip install --no-index --find-links=./package/ leveldb

# 批量下载，读取requirements.txt，将里面指定的包（包括依赖包）下载到本地某个目录，不安装
# pip download -d "./package/" -r requirements.txt

# 批量安装，pip从本地包安装
# pip install --no-index --find-links=./package/ -r requirements.txt

# 下载指定的包到指定文件夹
# pip download -d ./package/ gevent

# 离线安装本地的whl包，或者源码tar.gz包
# pip install --no-index --find-links=./package/ gevent
