 #!/usr/bin/env python3
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)


        while True:
            data = conn.recv(1024)
            if not data:
                break
            str_data = data.decode('utf-8')
            print(f'Client message: {str_data}')
            conn.sendall(data)
            
            msg = input('Your message: ').encode() #code str to bytes
            if msg == b'exit':
                break
            conn.sendall(msg)
            data = conn.recv(1024).decode('utf-8')