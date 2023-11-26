"""
URL configuration for Pagina_Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Pagina_Web.views import prueba, mapa, modismos, index, readfile, buscar_ubicacion, integrantes, sobre_nosotros, error_404_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('mapa/', mapa),
    path('modismos/', modismos),
    path('prueba/', prueba),
    path('integrantes/', integrantes),
    path('sobre_nosotros/', sobre_nosotros),
   path('modismos/<str:filtro>', readfile),
   path('buscador/', buscar_ubicacion, name='buscar_ubicacion')
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = error_404_view

