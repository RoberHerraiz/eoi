import socket

UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", UDP_PORT))
print("Escuchando por el puerto {}".format(UDP_PORT))

try:
    while True:
        
        try:
            data, addr = sock.recvfrom(512)

        except socket.timeout:
            continue

        print(addr)
        print(data)
        sock.sendto(b'Te he oido', addr)

except KeyboardInterrupt:
    sock.close()
