# Request: realizar peticiones
# HttpResponse: Enviar respuesta usando metodos http

from django.http import HttpResponse
from django.shortcuts import render


def mapabox(request):
    return render(request, 'miapp/mapa.html')
def prueba(request):
    return HttpResponse("Saludos a la fer porque llego TARDE")
def default(request):
    return render(request,"default/index.html")
def mapa(request):
    return render(request,"mapa/mapa.html")