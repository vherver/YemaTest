"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from pediatras.api_v1.endpoints import *

app_name = 'pediatras_v1'


urlpatterns = [
    path(r'', DoctorList.as_view(), name='Doctor_List_Creation'),
    path(r'<uuid:pk>/', DoctorDetail.as_view(), name='Doctor detail / Update'),
]
