from rest_framework import serializers

from citas.models import Citas


class CitasSerializer(serializers.ModelSerializer):
    """
    Serializador base para citas
    """

    patient_full_name = serializers.CharField(source="patient.full_name", read_only=True)
    doctor_full_name = serializers.CharField(source="doctor.full_name", read_only=True)
    office_full_info = serializers.CharField(source="consultorio.__str__", read_only=True)
    str_date = serializers.CharField(source="get_appointmentt_str_date", read_only=True)

    class Meta:
        model = Citas

        fields = ('id', 'doctor', 'doctor_full_name', 'consultorio', 'office_full_info',
                  'patient', 'patient_full_name',
                  'creation_date', 'active', 'appointment_date', 'str_date')


class CitasPacienteSerializer(serializers.ModelSerializer):
    """
    Serializador base para citas
    """

    doctor_full_name = serializers.CharField(source="doctor.full_name", read_only=True)
    office_full_info = serializers.CharField(source="consultorio.__str__", read_only=True)
    str_date = serializers.CharField(source="get_appointmentt_str_date", read_only=True)

    class Meta:
        model = Citas

        fields = ('doctor', 'doctor_full_name', 'consultorio', 'office_full_info',
                  'appointment_date', 'str_date')


class CitasPediatraSerializer(serializers.ModelSerializer):
    """
    Serializador base para citas
    """

    patient_full_name = serializers.CharField(source="patient.full_name", read_only=True)
    office_full_info = serializers.CharField(source="consultorio.__str__", read_only=True)
    str_date = serializers.CharField(source="get_appointmentt_str_date", read_only=True)

    class Meta:
        model = Citas

        fields = ('consultorio', 'office_full_info',
                  'patient', 'patient_full_name',
                  'creation_date', 'active', 'appointment_date', 'str_date')

