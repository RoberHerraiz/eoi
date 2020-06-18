from machine import Pin
import network
import utime as time
import usocket as socket

from credenciales import ssid, password # hay que crear el fichero credenciales

# Configurar hardware
led = Pin(2, Pin.OUT)


# Conexión wifi
led.value(0)
print('\nConectandose 2a wifi...', end='')
red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)
while not red.isconnected(): # Espera hasta que conecte
    time.sleep(0.1)
print('conectado!')
print(red.ifconfig())
led.value(1)

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)
    mensaje = b"Hola, mundo!"
    print(mensaje)
    sock.sendto(mensaje, ("192.168.1.255", 5005))
    # sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) # esto en usocket no funciona bien
    try:
        data, addr = sock.recvfrom(512)
        print(addr)
        print(data)
    except OSError: # TIMEOUT
        print("no hay respuesta")
    sock.close()
    led.value(0)
    time.sleep(0.1)
    led.value(1)
    time.sleep(1)
