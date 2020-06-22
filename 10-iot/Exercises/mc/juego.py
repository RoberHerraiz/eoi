import btree
from machine import Pin, I2C
import urandom as random
import utime as time

from credenciales import ssid, password
from mimqtt import Mimqtt


class Juego:
    def __init__(self, jugador):
        self.led = Pin(2, Pin.OUT)
        self.boton = Pin(0, Pin.IN)
        self.led.value(1)
        self.jugador = jugador
        self.mimqtt = Mimqtt()
        self.sensor = None

    def write_db(self, tiempo, jugador, modo):
        # tiempo, jugador, modo = str(tiempo), jugador.encode(), modo.encode()
        try:
            f = open('mydb', "r+b")
        except OSError:
            f = open('mydb', "w+b")
        self.db = btree.open(f)

        self.db[b'jugador'] = jugador
        self.db[b'tiempo'] = str(tiempo)
        self.db[b'modo'] = str(modo)
        self.db.flush()
        for word in self.db.values():
            print(word) # DEBUG
        self.db.close()
        f.close()
        self.start()

    def metodo_entrada(self, mode):
        self.sensor = mode

    def start(self):
        print()
        if self.sensor:
            print('Activa el sensor cuando se encienda el led')
        else:
            print("Pulsa el botón cuando se encienda el led")
        while True:
            self.encender_led_aleatorio()
            inicio = time.ticks_ms()
            self.apagar_led_boton()
            final = time.ticks_ms()
            tiempo = time.ticks_diff(final, inicio)
            if tiempo > 5000:
                print('Has tardado más de 5 segundos ({} ms)'.format(tiempo))
                print("\n")
                print('Reiniciando ...')
                self.start()
            elif tiempo < 10:
                if self.sensor:
                    print('El sensor estaba activado antes de encenderse el led')
                else:
                    print("El botón estaba activado antes de encenderse el led")
            else:
                print('Has apagado el botón en {} ms'.format(tiempo))
                if self.sensor:
                    metodo = "sensor"
                else:
                    metodo = "boton"
                self.mimqtt.enviar_mqtt(self.jugador, metodo, tiempo)
                time.sleep_ms(50)
                # self.write_db(self.jugador, metodo, tiempo)
                self.mimqtt.comprobar_mensajes()

    def encender_led_aleatorio(self):
        aleatorio = random.getrandbits(12)
        aleatorio += 3000
        time.sleep_ms(aleatorio)
        self.led.value(0)

    def apagar_led_boton(self):
        if self.sensor:
            while not self.led.value():
                proximidad = self.sensor.get_proximidad()
                if proximidad is not 0:
                    print("Sensor activado a {}!".format(proximidad))
                    self.led.value(1)
        else:
            while self.boton.value() == 1:
                time.sleep_ms(1)
            self.led.value(1)
