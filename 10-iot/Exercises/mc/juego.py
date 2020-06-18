from machine import Pin
import urandom as random
import utime as time

from mimqtt import Mimqtt
from credenciales import ssid, password

class Juego:
    def __init__(self, jugador):
        self.led = Pin(2, Pin.OUT)
        self.boton = Pin(0, Pin.IN)
        self.led.value(1)
        self.jugador = jugador
        self.mimqtt = Mimqtt()


    def start(self):
        while True:
            print()
            print('Pulsa el boton cuando se encienda el led')
            self.encender_led_aleatorio()
            inicio = time.ticks_ms()
            self.apagar_led_boton()
            final = time.ticks_ms()
            tiempo = time.ticks_diff(final, inicio)
            if tiempo > 5000:
                print('Has tardado más de 5 segundos')
                print("\n")
                print('Reiniciando ...')
            else:
                print('Has apagado el botón en {} ms'.format(tiempo))
                self.mimqtt.enviar_mqtt(self.jugador, tiempo)

    def encender_led_aleatorio(self):
        aleatorio = random.getrandbits(12)
        aleatorio += 3000
        time.sleep_ms(aleatorio)
        self.led.value(0)


    def apagar_led_boton(self):
        while self.boton.value() == 1:
            time.sleep_ms(1)
        self.led.value(1)
