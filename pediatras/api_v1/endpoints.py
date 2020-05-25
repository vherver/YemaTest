"""
Archivo base para Enpoints de aplicacion
"""
from rest_framework import generics

from YemaTest.paginator import Paginator
from pediatras.serializers import DoctorSerializer
from pediatras.models import Pediatra


class DoctorList(generics.ListCreateAPIView):
    """
        Enpoint para la creacion y listado de pediatras en aplicacion
    """
    serializer_class = DoctorSerializer
    pagination_class = Paginator
    queryset = Pediatra.objects.all().order_by('id')


class DoctorDetail(generics.RetrieveUpdateAPIView):
    """
        Enpoint para la detalle y actualizacion de informacion de pediatras
    """

    serializer_class = DoctorSerializer
    queryset = Pediatra.objects.all().order_by('id')
