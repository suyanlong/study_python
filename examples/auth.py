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
@click.option("--count_per_batch", default = 30)
@click.option("--buffer_duration", default = 3000000)
@click.option("--tx_verify_thread_num", default = 4)
@click.option("--tx_verify_num_per_thread", default = 300)
@click.option("--proposal_tx_verify_num_per_thread", default = 30)
@click.option("--tx_pool_limit", default = 0)
@click.option("--block_packet_tx_limit", default = 30000)
@click.option("--prof_start", default = 0)
@click.option("--prof_duration", default = 0)
@click.option("--path", default = "./", help = "config file path, default: ./ ")
def auth(count_per_batch, buffer_duration, tx_verify_thread_num, tx_verify_num_per_thread,
         proposal_tx_verify_num_per_thread, tx_pool_limit, block_packet_tx_limit, prof_start, prof_duration, path):
    """genrate auth config file"""

    data = dict()
    data["count_per_batch"] = count_per_batch
    data["buffer_duration"] = buffer_duration
    data["tx_verify_thread_num"] = tx_verify_thread_num
    data["tx_verify_num_per_thread"] = tx_verify_num_per_thread
    data["proposal_tx_verify_num_per_thread"] = proposal_tx_verify_num_per_thread
    data["tx_pool_limit"] = tx_pool_limit
    data["block_packet_tx_limit"] = block_packet_tx_limit
    data["prof_start"] = prof_start
    data["prof_duration"] = prof_duration
    dump_path = os.path.join(path, "auth.json")
    f = open(dump_path, "w")
    json.dump(data, f, indent = 4)
    f.close()


if __name__ == '__main__':
    auth()
