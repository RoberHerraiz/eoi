#!/usr/bin/env python3
import socket

# tcp://2.tcp.eu.ngrok.io:11512

HOST = '0.tcp.eu.ngrok.io'  # The server's hostname or IP address
PORT = 14510       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        string = input('> ')
        s.sendall(string.encode('utf-8'))
        print('server says: ', end='', flush=True)
        data = s.recv(1024)
        if not data or data == b'exit':
            break
        print(data.decode('utf-8')) 