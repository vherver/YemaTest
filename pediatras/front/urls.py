"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from pediatras.front.views import *

app_name = 'pediatras_front'


urlpatterns = [
    path(r'', pediatras_view, name='front all pediatrician'),
    path(r'<uuid:pediatra_id>/', pediatras_detail_view, name='Pediatrician detail'),

]
