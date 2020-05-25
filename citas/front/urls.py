"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from citas.front.views import *

app_name = 'clients_front'


urlpatterns = [
    path(r'', citas_view, name='front all appointments'),
]
