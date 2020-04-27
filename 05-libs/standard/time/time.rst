La Librería time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esté modulo proporciona funciones para trabajar con tiempos y fechas.
La mayoría de las funciones realizan llamadas al S.O. subyacente.

Algunas consideraciones y terminología:

  * UTC es el tiempo coordinado Universal, anteriormente
    conocido como GMT o Hora de Greenwich (El acrónimo UTC
    es un comprimiso entre el inglés y el francés)

  * DST es el ajuste de horario de verano (*Daylight Saving Time*)
    una modificacion de la zona horaria, normalmente de una
    hora, que se realiza durante parte del año. las reglas
    de los DST son, en la práctica, pura magia (dependen de
    las leyes locales) y pueden cambiar de año a año,

Los valores de tiempo devueltos por ``gmtime()``, ``localtime()`` y
``strptime()``, y aceptados por ``asctime()``, ``mktime()`` y
``strftime()`` son tuplas (En realidad, ``namedtuple``) de 9 enteros:
año, mes, dia, horas, minutos, segundos, día de la semana, día dentro
del año y un indicador de si se aplica o no el horario de verano.

Algunas funciones definidas en este módulo:

    ``time.time()``

        Devuelve el tiempo en segundos, en forma de número de coma
        flotante.


    ``time.gmtime([secs])``

        Convierte  un tiempo en segundos en una tupla de nueve elementos,
        en los cuales el flag final es siempre 0. Si no se indica
        el tiempo , se tomará el momento actual.

    ``time.localtime([secs])``

        Como ``gmtime()``, pero convertido a tiempo local. El indicador
        final se pone a uno si en ese momento estaba activo el horario de
        verano.

    ``time.mktime(t)``

        La inversa de ``localtime()``. Su argumento es
        una tupla de 9 elementos (Como el flag final es obligatorio,
        se puede poner -1 para indicar que no lo sabemos). Devuelve
        un número de segundos unix.

    ``time.sleep(secs)``

        Suspender la ejecución del programa durante el tiempo en segundos
        indicado como parámetro.

Ejercicio: Averiguar el día de la semana en que nacieron -O cualquier
otra fecha que les interese-.
