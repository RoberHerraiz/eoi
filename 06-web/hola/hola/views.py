from django.shortcuts import render

import datetime
# from django.http import HttpResponse

# Escribimos una vista (hace un request, devuelve un response)
def hola(request):
    return render(request, "hola.html", {
        "message": "hola, mundo molón",
        "ahora": datetime.datetime.now(),
    })