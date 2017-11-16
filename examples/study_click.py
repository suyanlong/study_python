#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import click


@click.command()
@click.option('--param', default = 1, help = '111')
def func(param):
    print param


if __name__ == '__main__':
    func()
