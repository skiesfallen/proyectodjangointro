# Request: realizar peticiones
# HttpResponse: Enviar respuesta usando metodos http

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"Index/index.html")
def mapa(request):
    return render(request,"Api/mapa/mapa.html")
def modismos(request):
    return render(request, "index/modismos.html")
def prueba(request):
    return render(request, "index/pruebas1.html")
def LogIn (request):
    return render(request, "Inicio_Sesion/LogIn.html")
def Register (request):
    return render(request, "Inicio_Sesion/Register.html")
def Modissmo (request):
    return render(request, "mod.html")