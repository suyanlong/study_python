#! /usr/bin/env python2
# -*- coding:utf-8 -*-
import fabric
from fabric.api import local


def hello():
    print("Hello world!")


def prepare_deploy():
    local("ls -al")
    print locals()


def env():
    print(fabric.state.env.user)
    print(fabric.state.env.password)
