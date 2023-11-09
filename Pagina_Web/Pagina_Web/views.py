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
    lista_palabras = [] #[0]: palabra    [1] definicion     [2] filtro
    for lineas in f:
        linea = lineas.strip().split('-')
        lista_palabras.append(linea)

    print(lista_palabras)        
    f.close()


    return render(request, "mod.html", {"diccionario_palabras" : lista_palabras} )


