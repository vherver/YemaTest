"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from pacientes.api_v1.endpoints import *

app_name = 'pacientes_v1'


urlpatterns = [
    # path(r'', ClientList.as_view(), name='Client_List_Creation'),
    # path(r'<str:pk>/', ClientDetail.as_view(), name='Client detail / Update'),
]
