#!/usr/bin/env python3
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
   
    while True:
        msg = input('Your message: ').encode() #code str to bytes
        s.sendall(msg)
        data = s.recv(1024).decode('utf-8')
        if msg == b'exit':
            break

        data = s.recv(1024)
        if not data:
            break
        str_data = data.decode('utf-8')
        print(f'Client message: {str_data}')
        s.sendall(data)



