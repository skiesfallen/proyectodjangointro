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

def readfile(request):
    f = open('modismos.txt', 'r', encoding="UTF-8")
    dic = {}
    for lineas in f:
        linea = lineas.strip().split('-')
        dic[linea[0]] = linea[1]
    print(dic)
    f.close()


    return render(request, "mod.html", {"diccionario" : dic} )


