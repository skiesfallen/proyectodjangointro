# Request: realizar peticiones
# HttpResponse: Enviar respuesta usando metodos http

from django.http import HttpResponse

def prueba(request):
    return HttpResponse("Prueba")
def default(request):
    return HttpResponse("Aqui descifrando los misterios de Django, salu2")