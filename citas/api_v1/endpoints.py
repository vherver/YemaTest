"""
Archivo base para Enpoints de aplicacion
"""

from rest_framework import generics

from YemaTest.paginator import Paginator
from citas.serializers import CitasSerializer
from citas.models import Citas


class CitasList(generics.ListCreateAPIView):
    """
        Enpoint para la creacion y listado de Citas en aplicacion
    """
    serializer_class = CitasSerializer
    pagination_class = Paginator
    queryset = Citas.objects.all().order_by('-appointment_date')


class CitasDetail(generics.RetrieveUpdateAPIView):
    """
        Enpoint para la detalle y actualizacion de informacion de Citas
    """

    serializer_class = CitasSerializer
    queryset = Citas.objects.all().order_by('id')
