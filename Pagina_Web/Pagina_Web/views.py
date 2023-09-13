# Request: realizar peticiones
# HttpResponse: Enviar respuesta usando metodos http

from django.http import HttpResponse
from django.shortcuts import render

def prueba(request):
    return HttpResponse("Saludos a la fer porque llego TARDE")
def default(request):
    return HttpResponse("Aqui descifrando los misterios de Django, salu2")