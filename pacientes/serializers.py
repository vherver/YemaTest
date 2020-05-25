from rest_framework import serializers

from pacientes.models import Paciente


class PacientSerializer(serializers.ModelSerializer):
    """
    Serializador base para pacientes
    """
    class Meta:
        model = Paciente

        fields = '__all__'
