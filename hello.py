#! /usr/bin/env python2
# -*- coding:utf-8 -*-


import click


@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')
