import ujson as json

from umqtt.simple import MQTTClient


class Mimqtt():

    def enviar_mqtt(self, nombre, tiempo):
        id_cliente = "12hi3b1i2n98dno2jnd921"
        mqtt_server = "broker.hivemq.com"
        topic = b'curso_eoi'
        datos = {
            "Nombre": nombre,
            "Tiempo": tiempo
        }
        datos = json.dumps(datos)
        client = MQTTClient(id_cliente, mqtt_server)
        client.connect()
        client.publish(topic, datos)
