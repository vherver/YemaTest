from rest_framework import serializers

from consultorio.models import Consultorio


class ConsultorioSerializer(serializers.ModelSerializer):
    """
    Serializador base para consultorio
    """
    class Meta:
        model = Consultorio

        fields = '__all__'
