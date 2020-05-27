"""
Archivo base para gestion de URLs para acceso al API de la aplicacion
"""

from django.urls import path

from pacientes.front.views import *

app_name = 'pacientes_front'


urlpatterns = [
    path(r'', pacientes_view, name='front all patientes'),
    path(r'<uuid:paciente_id>/', pacientes_detail_view, name='Patients detail'),
]
