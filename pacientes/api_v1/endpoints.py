"""
Archivo base para Enpoints de aplicacion
"""
from rest_framework import generics

from YemaTest.paginator import Paginator
from pacientes.serializers import PacientSerializer
from pacientes.models import Paciente


class PatientList(generics.ListCreateAPIView):
    """
        Enpoint para la creacion y listado de pacientes en aplicacion
    """
    serializer_class = PacientSerializer
    pagination_class = Paginator
    queryset = Paciente.objects.all().order_by('id')


class PatientDetail(generics.RetrieveUpdateAPIView):
    """
        Enpoint para la detalle y actualizacion de informacion de pacientes
    """

    serializer_class = PacientSerializer
    queryset = Paciente.objects.all().order_by('id')
