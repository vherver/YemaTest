"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from consultorio.front.views import *

app_name = 'consultorio_front'


urlpatterns = [
    path(r'', consultorio_view, name='front all consultorio'),
]
