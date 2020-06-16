from machine import Pin
import network
import utime as time

from credenciales import ssid, password # hay que crear el fichero credenciales
from corneto import Corneto

# Configurar hardware
led = Pin(2, Pin.OUT)


# Conexión wifi
led.value(0)
print('\nConectandose a wifi...', end='')
red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)
while not red.isconnected(): # Espera hasta que conecte
    time.sleep(0.1)

print('conectado!')
print(red.ifconfig())
led.value(1)
