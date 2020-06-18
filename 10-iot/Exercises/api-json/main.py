import ujson as json
from machine import Pin
import utime as time
import network
import urequests as requests

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


def get_rate(currency):
    url = "https://api.coindesk.com/v1/bpi/currentprice/{}.json".format(currency)
    r = requests.get(url)
    if r.status_code is not 200:
        print("Error al acceder a coindesk, reseteando...")
        print('r.status')
        print('r.content')
        time.sleep(10)
        reset()
    resultado = r.content.decode()
    data = json.loads(resultado)
    rate = data["bpi"]["USD"]["rate"]
    return (rate)

crypto_code = "BTC"

while True:
    rate = get_rate(crypto_code)
    print('El precio del {} es {} USD'.format(crypto_code, rate))
    time.sleep(10)
