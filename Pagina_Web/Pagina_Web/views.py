# Request: realizar peticiones
# HttpResponse: Enviar respuesta usando metodos http

from django.http import HttpResponse
from django.shortcuts import render


def prueba(request):
    return HttpResponse("Saludos a la fer porque llego TARDE")
def default(request):
    return render(request,"index.html")
def mapa(request):
    return render(request,"mapa.html")
def modismos(request):
    return render(request, "modismos.html")
def index(request):
    return render(request, "pruebas1.html")