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
@click.option('--name', help = 'The person to greet.')
def hello(name):
    click.secho('Hello %s!' % name, fg = 'red', underline = True)
    click.secho('Hello %s!' % name, fg = 'yellow', bg = 'black')


# if __name__ == '__main__':
#     hello()


@click.group()
@click.option('--index', help = 'index')
def gpfun(index):
    pass


@click.command()
@click.option('--name', prompt = 'enter your name here: ',
              help = 'greet to given name')
def hello(name):
    click.echo('Hello World! hello %s' % name)


@click.command()
@click.option('--name', prompt = 'enter your name here: ',
              help = 'greet to given name')
def hello1(name):
    click.echo('Hello World! hello %s' % name)


@click.command()
@click.option('--message', '-m', multiple = True)
def commit(message):
    click.echo('\n'.join(message))
    click.echo('\n'.join(message))
    click.echo('\n'.join(message))
    click.echo('\n'.join(message))


gpfun.add_command(hello)
gpfun.add_command(hello1)
gpfun.add_command(commit)


# @click.group()
# @click.option('--debug/--no-debug', default = False)
# def cli(debug):
#     click.echo('Debug mode is %s' % ('on' if debug else 'off'))
#
#
# @cli.command()
# def sync():
#     click.echo('Synching')
#
#
# if __name__ == '__main__':
#     cli()
#
# @click.group()
# @click.option('--debug/--no-debug', default=False)
# @click.pass_context
# def cli(ctx, debug):
#     print debug
#     ctx.obj['DEBUG'] = debug
#
# @cli.command()
# @click.pass_context
# def sync(ctx):
#     click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
#
# @cli.command()
# @click.pass_context
# def sync1(ctx):
#     click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
#
#
# if __name__ == '__main__':
#     cli(obj={})

#
# @click.group(invoke_without_command = True)
# @click.pass_context
# def cli(ctx):
#     if ctx.invoked_subcommand is None:
#         click.echo('I was invoked without subcommand')
#     else:
#         click.echo('I am about to invoke %s' % ctx.invoked_subcommand)
#
#     click.echo("=========分割线======")
#
#
# @cli.command()
# def sync():
#     click.echo('The subcommand')
#
#
# if __name__ == '__main__':
#     cli(obj = {})


@click.command()
@click.option('--count', default = 1, help = 'Number of greetings.')
@click.option('--name', prompt = 'Your name',
              help = 'The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


# 清屏命令:clear
# click.clear()


@click.command()
def less():
    click.echo_via_pager('\n'.join('Line %d' % idx
                                   for idx in range(200)))


if __name__ == '__main__':
    # less()
    click.echo('Path: %s' % click.format_filename(b'foo.txt'))
