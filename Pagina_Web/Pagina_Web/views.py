# Request: realizar peticiones
# HttpResponse: Enviar respuesta usando metodos http

from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request,"Index/index.html")
def mapa(request):
    return render(request,"Api/mapa/mapa.html")
def modismos(request):
    f = open('modismos.txt', 'r', encoding="UTF-8")
    lista_palabras = [] #[0]: palabra    [1] definicion     [2] filtro

    for lineas in f:
        
        linea = lineas.strip().split('-')
        lista_palabras.append(linea)

    
    f.close()


    return render(request, "Index/modismos.html", {"diccionario_palabras" : lista_palabras} )


def prueba(request):
    return render(request, "index/pruebas1.html")


def readfile(request, filtro):
    f = open('modismos.txt', 'r', encoding="UTF-8")
    lista_palabras = [] #[0]: palabra    [1] definicion     [2] filtro     [3] Buscado
    if "_" in filtro:
        b = filtro.split("_")
        a = ''
        for palabra in b:
            a+=palabra+" "
        for lineas in f:
            linea = lineas.strip().split('-')
            linea.append(a[:-1])
            lista_palabras.append(linea)
        
        
    else:
        for lineas in f:
            linea = lineas.strip().split('-')
            linea.append(filtro)
            lista_palabras.append(linea)
      
    f.close()


    return render(request, "mod.html", {"diccionario_palabras" : lista_palabras})


