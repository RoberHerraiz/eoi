from credenciales import ssid, password
import network
import utime as time
from machine import Pin, I2C

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

# conectar_wifi()
# juego = Juego("Rober .H")
# juego.start()

# from machine import Pin, I2C
i2c = I2C(sda=Pin(5), scl=Pin(4))
i2c.scan() #comprobamos que es 57

ADDR_SENSOR = 0x39

i2c.writeto(ADDR_SENSOR, bytearray([0x12|0xA0])) # LE AVISAMOS QUE VAMOS QUEREMOS LEER
resultado = i2c.readfrom(ADDR_SENSOR, 1)[0] # LE INDICAMOS QUE QUEREMOS LEER UN 1
print(resultado)
