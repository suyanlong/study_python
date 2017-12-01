# !/usr/bin/env python
# coding=utf-8

import json
import os

import click


@click.command()
@click.option("--http", "-h", default = True, type = bool, help = "enable HTTP protocol,default: true")
@click.option("--http_port", "-H", default = 1337, help = "listen HTTP protocol port,default: 1337")
@click.option("--ws", "-w", default = True, type = bool, help = "enable WebSocket protocol,default: true")
@click.option("--ws_port", "-W", default = 4337, help = "listen WebSocket protocol,default: 4337")
@click.option("--path", default = "./", help = "config file path, default: ./ ")
def jsonrpc(http, http_port, ws, ws_port, path):
    """genrate jsonrpc config file"""

    profile_config = dict(enable = False, flag_prof_start = 0, flag_prof_duration = 0)
    http_config = dict(enable = http, thread_number = 200,
                       listen_ip = "0.0.0.0", listen_port = http_port,
                       timeout = 3)

    ws_config = dict(
        enable = ws, thread_number = 2,
        listen_ip = "0.0.0.0", listen_port = ws_port,
        max_connections = 800, queue_size = 200,
        panic_on_new_connection = False, panic_on_shutdown = False,
        fragments_capacity = 100, fragments_grow = True,
        fragment_size = 65535, in_buffer_capacity = 2048,
        in_buffer_grow = True, out_buffer_capacity = 2048,
        out_buffer_grow = True, panic_on_internal = True,
        panic_on_capacity = False, panic_on_protocol = False,
        panic_on_encoding = False, panic_on_queue = False,
        panic_on_io = False, panic_on_timeout = False,
        shutdown_on_interrupt = True, masking_strict = False,
        key_strict = False, method_strict = False,
        encrypt_server = False, tcp_nodelay = False
    )

    data = dict()
    data["with_capacity"] = 1000
    data["profile_config"] = profile_config
    data["http_config"] = http_config
    data["ws_config"] = ws_config
    data["new_tx_flow_config"] = dict(count_per_batch = 30, buffer_duration = 30000000)

    dump_path = os.path.join(path, "jsonrpc.json")
    f = open(dump_path, "w")
    json.dump(data, f, indent = 4)
    f.close()


if __name__ == '__main__':
    jsonrpc()
