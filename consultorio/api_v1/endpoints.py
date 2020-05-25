"""
Archivo base para Enpoints de aplicacion
"""

from rest_framework import generics

from YemaTest.paginator import Paginator

from consultorio.serializers import ConsultorioSerializer
from consultorio.models import Consultorio


class ConsultorioList(generics.ListCreateAPIView):
    """
        Enpoint para la creacion y listado de consultorios en aplicacion
    """
    serializer_class = ConsultorioSerializer
    pagination_class = Paginator
    queryset = Consultorio.objects.all().order_by('id')


class ConsultorioDetail(generics.RetrieveUpdateAPIView):
    """
        Enpoint para la detalle y actualizacion de informacion de consultorios
    """

    serializer_class = ConsultorioSerializer
    queryset = Consultorio.objects.all().order_by('id')
