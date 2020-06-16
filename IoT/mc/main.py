from machine import Pin
import utime as time
import network


from credenciales import ssid, password


led = Pin(2, Pin.OUT)


led.value(0)
print('\nConectandose a la wifi...', end='')
red = network.WLAN(network.STA_IF)
red.active(True)
red.connect(ssid, password)
while not red.isconnected():
    time.sleep(0.1)
print('conectado!')
print(red.ifconfig())
led.value(1)

import upip
upip.install('micropython-urequests')

#
# codigo_ciudad = "773692"
# url = "https://www.metaweather.com/api/location/{}/".format(codigo_ciudad)
# r = requests.get(url)
# if r.status_code is not 200:
#     print("Error al acceder a metaweather, reseteando...")
#     reset()
# print('Todo ok')
# resultado = r.content.decode()
# print(resultado)
#
# with open("respuesta_api_json", "r") as jf:
#

# while True:
#     time.sleep(1)
