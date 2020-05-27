from rest_framework import serializers

from pacientes.models import Paciente


class PacientSerializer(serializers.ModelSerializer):
    """
    Serializador base para pacientes
    """

    pacient_full_name = serializers.CharField(source="get_full_name", read_only=True)

    class Meta:
        model = Paciente

        fields = '__all__'

        fields.__add__('pacient_full_name')
