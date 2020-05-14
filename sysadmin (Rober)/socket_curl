import socket

buffer = b'' 
with socket.socket() as s: 
    s.connect(('ifconfig.io', 80)) 
    s.send(b'GET / HTTP/1.1\r\nHost: ifconfig.io\r\nUser-Agent: curl\r\n\r\n') 
    buffer = s.recv(4096)

buffer_str = buffer.decode('ascii').split('\r\n\r\n')

print(buffer_str[1].rstrip()) 
