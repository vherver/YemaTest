"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from pacientes.api_v1.endpoints import *

app_name = 'pacientes_v1'


urlpatterns = [
    path(r'', PatientList.as_view(), name='Patients_List_Creation'),
    path(r'<uuid:pk>/', PatientDetail.as_view(), name='Patients detail / Update'),
]
