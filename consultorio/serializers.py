from rest_framework import serializers

from consultorio.models import Consultorio


class ConsultorioSerializer(serializers.ModelSerializer):
    """
    Serializador base para consultorio
    """

    consultorio_full_name = serializers.CharField(source="get_full_name", read_only=True)

    class Meta:
        model = Consultorio

        fields = '__all__'

        fields.__add__('consultorio_full_name')

