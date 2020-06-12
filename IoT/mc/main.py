from machine import Pin, PWM, ADC, Timer
import utime

boton_pulsado = False
tiempo_inicio_boton = 0

def boton_callback(x):
    global boton_pulsado, tiempo_inicio_boton
    boton_pulsado = True
    tiempo_inicio_boton = utime.ticks_ms()


boton = Pin(0, Pin.IN)
boton.irq(boton_callback, trigger=Pin.IRQ_FALLING)

while True:
    print("x")
    if boton_pulsado:
        print("boton pulsado marca {}".format(tiempo_inicio_boton))
        ahora =  utime.ticks_ms()
        tiempo_boton = utime.ticks_diff(ahora, tiempo_inicio_boton)

        print(tiempo_boton)
        if tiempo_boton < 50:
            utime.sleep_ms(50-tiempo_boton)
        estado = boton.value()
        if estado:
            print("esto es ruido, no hacer nada")
        else:
            print("boton pulsado de verdad")
        utime.sleep(0.5) #antirrebotes
        boton_pulsado = False
    utime.sleep(0.1)
