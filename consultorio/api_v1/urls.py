"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from consultorio.api_v1.endpoints import *

app_name = 'consultorios_v1'


urlpatterns = [
    path(r'', ConsultorioList.as_view(), name='Consultorio_List_Creation'),
    path(r'<uuid:pk>/', ConsultorioDetail.as_view(), name='Consultorio detail / Update'),
]
