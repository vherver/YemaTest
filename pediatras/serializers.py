from rest_framework import serializers

from pediatras.models import Pediatra


class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializador base para pediatra
    """
    class Meta:
        model = Pediatra

        fields = '__all__'
