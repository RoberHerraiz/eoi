import ujson as json
import utime as time

from umqtt.simple import MQTTClient


class Mimqtt():

    def __init__(self):
        id_cliente = "12hi3b1i2n98dno2jnd921"
        mqtt_server = "broker.hivemq.com"
        self.client = MQTTClient(id_cliente, mqtt_server)
        self.client.set_callback(self.mqtt_callback)
        self.client.connect()
        self.client.subscribe(b'curso_eoi')

    def enviar_mqtt(self, nombre, metodo, tiempo):
        topic = b'curso_eoi'
        datos = {
            "Nombre": nombre,
            "Metodo": metodo,
            "Tiempo": tiempo
        }
        datos = json.dumps(datos)
        self.client.publish(topic, datos)

    def mqtt_callback(self, topic, msg):
        try:
            datos = json.loads(msg.decode())
        except ValueError:
            print("mensaje invalido")
        print("me llego por '{}' esto: {}".format(topic, msg))

    def comprobar_mensajes(self):
        for i in range(10):
            self.client.check_msg()
            time.sleep_ms(10)
