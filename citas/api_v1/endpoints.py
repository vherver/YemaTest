"""
Archivo base para Enpoints de aplicacion
"""

from rest_framework import generics,  status
from rest_framework.response import Response



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


class CitasDetailPatient(generics.ListAPIView):
    """
        Enpoint para la creacion y listado de Citas en de un paciente
    """
    serializer_class = CitasSerializer
    pagination_class = Paginator

    def get_queryset(self):
        query_set = Citas.objects.filter(patient__id=str(self.kwargs['pacient_id']))
        return query_set


class CitasDetailPediatra(generics.ListAPIView):
    """
        Enpoint para la creacion y listado de Citas en de un pediatra
    """
    serializer_class = CitasSerializer
    pagination_class = Paginator

    def get_queryset(self):
        query_set = Citas.objects.filter(doctor__id=str(self.kwargs['pediatra_id']))
        return query_set


class CitasDetailConsultorio(generics.ListAPIView):
    """
        Enpoint para la creacion y listado de Citas en de un consultorio
    """
    serializer_class = CitasSerializer
    pagination_class = Paginator

    def get_queryset(self):
        query_set = Citas.objects.filter(consultorio__id=str(self.kwargs['consultorio_id']))
        return query_set
