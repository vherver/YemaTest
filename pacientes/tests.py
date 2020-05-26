from rest_framework.test import APITestCase
from rest_framework import status

from pacientes.models import Paciente


class PacientesAPITestCase(APITestCase):
    """Test para creacion de pacientes"""

    def setUp(self):
        self.app_client = Paciente.objects.create(
            name="Victor",
            last_name="Herver",
            mother_name="Segura",
            father_name="Guadalupe Segura Delgado",
            phone="5515336642",
            birthdate="2016-07-16",
            gender="M",
            email="vicherver@gmail.com"
        )

    def test_pacient_list(self):
        """Verifica que el enpoint de obtencion de lista de pacientes responda con 200"""
        url = '/api/v1/pacientes/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_pacient_creation(self):
        """Verifica que el enpoint de creacion de pacientes funcione correctamente"""
        url = '/api/v1/pacientes/'
        data = {
                    "name": "Victor",
                    "last_name": "Herver",
                    "mother_name": "Segura",
                    "father_name": "Guadalupe Segura Delgado",
                    "phone": "5515336643",
                    "birthdate": "2016-07-16",
                    "gender": "M",
                    "email": "vicherve000r@gmail.com"
                }
        request = self.client.post(url, data)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_client_pacient_bad_request(self):
        """Verifica que el enpoint de creacion de pacientes con datos no esperados"""
        url = '/api/v1/pacientes/'
        data = {
                "nombre": "Usuario de Prueba"
                }
        request = self.client.post(url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_specific_pacient(self):
        """Verifica que el enpoint para obtener un pacientes por id"""
        url = '/api/v1/pacientes/{}/'.format(self.app_client.id)
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_specific_pacient_not_found(self):
        """Verifica que el enpoint para obtener un pacientes por id no encontrado"""
        url = '/api/v1/pacientes/AAA/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_pacient(self):
        """Verifica que el enpoint para actualizar pacientes"""
        url = '/api/v1/pacientes/{}/'.format(self.app_client.id)

        data = {
                "name": "Ernesto"
                }

        request = self.client.patch(url, data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
