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

# pip install --editable .