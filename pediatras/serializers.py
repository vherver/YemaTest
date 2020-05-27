from rest_framework import serializers

from pediatras.models import Pediatra


class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializador base para pediatra
    """

    pediatra_full_name = serializers.CharField(source="get_full_name", read_only=True)

    class Meta:
        model = Pediatra

        fields = '__all__'

        fields.__add__('pediatra_full_name')

