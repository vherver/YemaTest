from rest_framework.test import APITestCase
from rest_framework import status

from citas.models import Citas
from consultorio.models import Consultorio
from pacientes.models import Paciente
from pediatras.models import Pediatra


class CitasAPITestCase(APITestCase):
    """Test para creacion de citas"""

    def setUp(self):
        self.app_office = Consultorio.objects.create(
            hospital="Hospital 1",
            office="305-A"
        )

        self.app_pacient = Paciente.objects.create(
            name="Victor",
            last_name="Herver",
            mother_name="Segura",
            father_name="Guadalupe Segura Delgado",
            phone="5515336642",
            birthdate="2016-07-16",
            gender="M",
            email="vicherver@gmail.com"
        )

        self.app_pediatrician = Pediatra.objects.create(
            name="Julio",
            last_name="Rodiguez",
            mother_name="Mendoza",
            phone="5512345678",
            mail="rjm123456789@gmail.com",
        )

        self.app_appointment = Citas.objects.create(
            doctor=self.app_pediatrician,
            consultorio=self.app_office,
            patient=self.app_pacient,
            appointment_date="2020-05-28 18:00:00"
        )

    def test_appointment_list(self):
        """Verifica que el enpoint de obtencion de lista de citas responda con 200"""
        url = '/api/v1/citas/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_appointment_creation(self):
        """Verifica que el enpoint de creacion de citas funcione correctamente"""
        url = '/api/v1/citas/'
        data = {
                "doctor": str(self.app_pediatrician.id),
                "consultorio": str(self.app_office.id),
                "patient": str(self.app_pacient.id),
                "appointment_date": "2020-05-28 18:30:00"
            }

        request = self.client.post(url, data)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_appointment_bad_request(self):
        """Verifica que el enpoint de creacion de citas con datos no esperados"""
        url = '/api/v1/citas/'
        data = {
                "nombre": "Usuario de Prueba"
                }
        request = self.client.post(url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_specific_appointment(self):
        """Verifica que el enpoint para obtener un citas por id"""
        url = '/api/v1/citas/{}/'.format(self.app_appointment.id)
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_specific_appointment_not_found(self):
        """Verifica que el enpoint para obtener un consultorios por id no encontrado"""
        url = '/api/v1/citas/AAA/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_appointment(self):
        """Verifica que el enpoint para actualizar citas"""
        url = '/api/v1/citas/{}/'.format(self.app_appointment.id)

        data = {
                "appointment_date": "2020-05-28 17:00:00"
                }

        request = self.client.patch(url, data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
