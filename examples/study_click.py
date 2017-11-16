#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import click


@click.command()
@click.option('--param', default = 1, help = '111')
def func(param):
    print param


@click.command()
@click.option('--rate', type = float, help = 'rate vale')
def show(rate):
    click.echo('rate :%s' % rate)


# if __name__ == '__main__':
    # func()
    # show()


@click.command()
@click.option('--password', prompt = True, hide_input = True, confirmation_prompt = True)
def input_password(password):
    click.echo('password: %s' % password)


# if __name__ == '__main__':
#     input_password()


@click.command()
@click.option('--name', help='The person to greet.')
def hello(name):
    click.secho('Hello %s!' % name, fg='red', underline=True)
    click.secho('Hello %s!' % name, fg='yellow', bg='black')

if __name__ == '__main__':
    hello()