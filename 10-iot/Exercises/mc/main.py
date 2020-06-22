from machine import Pin, I2C
import network
import utime as time

from credenciales import ssid, password
from apds9930 import APDS9930
from juego import Juego

def conectar_wifi():
    print('\nConectandose a la wifi...', end='')
    red = network.WLAN(network.STA_IF)
    red.active(True)
    red.connect(ssid, password)
    while not red.isconnected():
        time.sleep(0.1)
    print('conectado!')
    print(red.ifconfig())


i2c=I2C(sda=Pin(4), scl=Pin(5))
try:
    sensor = APDS9930(i2c)
    sensor.activar_proximidad()
except Exception as e:
    sensor = None

conectar_wifi()
juego = Juego("Rober .H")
juego.metodo_entrada(sensor)
juego.start()
