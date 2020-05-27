"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from citas.api_v1.endpoints import *

app_name = 'citas_v1'


urlpatterns = [
    path(r'', CitasList.as_view(), name='Citas_List_Creation'),
    path(r'<uuid:pk>/', CitasDetail.as_view(), name='Citas detail / Update'),
    path(r'pacient/<uuid:pacient_id>/', CitasDetailPatient.as_view(), name='Citas detail '),
    path(r'pediatra/<uuid:pediatra_id>/', CitasDetailPediatra.as_view(), name='Citas detail'),
    path(r'consultorios/<uuid:consultorio_id>/', CitasDetailConsultorio.as_view(), name='Citas detail'),
]
