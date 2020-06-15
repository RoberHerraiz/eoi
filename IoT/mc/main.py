import network
import usocket as socket
from machine import Pin

def web_page(estado):
    html = """<html><head> <title>Ejemplo 1</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:;base64,iVBORw0KGgo="><style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
    h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
    border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
    .button2{background-color: #4286f4;}</style></head><body> <h1>CONTROL DE LED</h1>
    <p>Estado LED: <strong> """ + estado + """ </strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
    <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
    return html

led = Pin(2, Pin.OUT)
led.value(1)

red = network.WLAN(network.AP_IF)
red.active(True)
red.config(essid="MicroPython", password="12345678")

print(red.ifconfig())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 80))
sock.listen(5)
# sock.settimeout(30)

while True:
    print('Esperando conexion...')
    conn, addr = sock.accept()
    print(addr)
    request = conn.recv(1024)
    request_str = request.decode()
    print(request_str)
    respuesta = '<h1>Hola, mundo</h1> yo soy Rober'
    ledon = request_str.find("/?led=on")
    print(ledon)
    ledoff = request_str.find("/?led=off")
    print(ledoff)

    estado_led = led.value()
    estado_str = "ENCENDIDO" if not estado_led else "APAGADO"

    if  ledon == 4:
        led.value(0)
        respuesta = "Led encendido"
    elif ledoff == 4:
        respuesta = "Led apagado"
        led.value(1)

    conn.sendall('HTTP/1.1 200 OK\n')
    conn.sendall('Content-Type: text/html\n')
    conn.sendall('Connection: close\n\n')
    conn.sendall(web_page(estado_str))
    conn.close()
