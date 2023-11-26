# Request: realizar peticiones
# HttpResponse: Enviar respuesta usando metodos http

from django.http import HttpResponse
from django.shortcuts import render
import requests


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
    return render(request, "errores/Error404.html")


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

def buscar_ubicacion(request):
    if request.method == 'POST':
        lugar = request.POST.get('ubicacion', '')  # Obtiene la ubicación del formulario
        if lugar:
            coordenadas = obtener_coordenadas(lugar)
            print("DATOS:   ",coordenadas)
            return render(request, 'Api/mapa/mapa_busqueda.html', {'coordenadas': coordenadas})
        
        else:
            mensaje_error = 'Por favor, ingresa una ubicación.'
            return render(request, 'Api/mapa/mapa_busqueda.html', {'error': mensaje_error})
        
    else:
        return render(request, 'Api/mapa/mapa_busqueda.html')
    
def obtener_coordenadas(lugar):
    api_key = 'pk.eyJ1Ijoic2VzdGF5dCIsImEiOiJjbG4yMjdnNXcwM3huMnFuaGQ0b2pvZmNjIn0.JaDwRJbv84xiaL48MmZDkg'
    endpoint = 'https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json'
    url = endpoint.format(place=lugar)
    params = {'access_token': api_key}

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data.get('features'):
            feature = data['features'][0]
            nombre = feature['place_name']
            coordenadas = feature['geometry']['coordinates']
            return {'nombre': nombre, 'coordenadas': coordenadas}
    return None

def integrantes(request):
     return render(request, "index/integrantes.html")

def sobre_nosotros(request):
    return render(request,"index/sobre_nosotros.html")

def error_404_view(request, exception):
    return render(request,'Errores/Error404.html')