# -*- coding: utf-8 -*-
# 2023/2/7
# create by: snower

import sevent

PORT = 8000
SSH_ADDRES = ("127.0.0.1", 22)
HTTP_ADDRES = ("127.0.0.1", 80)
HTTPS_ADDRES = ("127.0.0.1", 443)

async def do_tcp_port_forward(conn):
    buffer = await conn.recv()
    data = buffer.join()

    forward_address = HTTP_ADDRES
    if b'SSH' == data[:3]:
        forward_address = SSH_ADDRES
    elif b'\x16\x03' == data[:2]:
        forward_address = HTTPS_ADDRES
    pconn = sevent.tcp.Socket()
    pconn.enable_nodelay()
    pconn.connect(forward_address)
    conn.link(pconn)

async def tcp_port_forward_server():
    server = sevent.tcp.Server()
    server.enable_reuseaddr()
    server.enable_nodelay()
    server.listen(("0.0.0.0", PORT))

    while True:
        conn = await server.accept()
        sevent.go(do_tcp_port_forward, conn)

sevent.run(tcp_port_forward_server)
