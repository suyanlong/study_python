#! /usr/bin/env python2
# -*- coding:utf-8 -*-


# {
#   "count_per_batch": 30,
#   "buffer_duration": 3000000,
#   "tx_verify_thread_num": 4,
#   "tx_verify_num_per_thread": 300,
#   "proposal_tx_verify_num_per_thread": 30,
#   "tx_pool_limit": 0,
#   "block_packet_tx_limit": 30000,
#   "prof_start": 0,
#   "prof_duration": 0
# }


import json
import os
import click


@click.command()
@click.option("--path", default = "./", help = "config file path, default: ./ ")
def auth(path):
    _auth(path)


def _auth(path = './'):
    """genrate auth config file"""

    data = dict()
    data["count_per_batch"] = 30
    data["buffer_duration"] = 3000000
    data["tx_verify_thread_num"] = 4
    data["tx_verify_num_per_thread"] = 300
    data["proposal_tx_verify_num_per_thread"] = 30
    data["tx_pool_limit"] = 0
    data["block_packet_tx_limit"] = 30000
    data["prof_start"] = 0
    data["prof_duration"] = 0
    dump_path = os.path.join(path, "auth.json")
    f = open(dump_path, "w")
    json.dump(data, f, indent = 4)
    f.close()


if __name__ == '__main__':
    auth()
