#! /usr/bin/env python2
# -*- coding:utf-8 -*-


# !/usr/bin/env python
# coding=utf-8

import json
import os
import click


@click.command()
@click.option("--test", "-p", default = True, type = bool, help = "enable test,default: true")
@click.option("--duration", "-d", default = 3000, help = "consensus duration, default: 1337")
@click.option("--consensus", "-c", default = "tendermint", help = "consensus name defalut: 'tendermint'")
@click.option("--path", default = "./", help = "config file path, default: ./")
def consensus(test, duration, consensus, path):
    _consensus(test, duration, consensus, path)


def _consensus(test = True, duration = 3000, consensus = 'tendermint', path = './'):
    secret_path = os.path.join(path, "privkey")
    with open(secret_path, "r") as secret_key:
        signer = secret_key.read()
    data = dict()
    params = dict(duration = duration, is_test = test, signer = signer)
    data["name"] = consensus
    data["engine"] = dict(Tendermint = dict(params = params)) if consensus == "tendermint" else dict(
        AuthorityRound = dict(params = params))
    dump_path = os.path.join(path, "consensus.json")
    with open(dump_path, "w") as f:
        json.dump(data, f, indent = 4)


if __name__ == '__main__':
    consensus()
