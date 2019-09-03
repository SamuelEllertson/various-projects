#!/usr/bin/env python

import socket
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    
    while True:
        text = input("> ")

        if text == "exit":
            break

        s.sendall(bytes(text, encoding="utf-8"))
    
