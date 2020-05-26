from rest_framework.test import APITestCase
from rest_framework import status

from pediatras.models import Pediatra


class PediatraAPITestCase(APITestCase):
    """Test para creacion de pediatras"""

    def setUp(self):
        self.app_client = Pediatra.objects.create(
            name="Julio",
            last_name="Rodiguez",
            mother_name="Mendoza",
            phone="5512345678",
            mail="rjm123456789@gmail.com",
        )

    def test_pediatrician_list(self):
        """Verifica que el enpoint de obtencion de lista de pediatras responda con 200"""
        url = '/api/v1/pediatras/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_pediatrician_creation(self):
        """Verifica que el enpoint de creacion de pediatras funcione correctamente"""
        url = '/api/v1/pediatras/'
        data = {
                    "name": "Norma",
                    "last_name": "Rodiguez",
                    "mother_name": "Mendoza",
                    "phone": "5598765432",
                    "mail": "96385271@gmail.com",
                }
        request = self.client.post(url, data)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_client_pediatrician_bad_request(self):
        """Verifica que el enpoint de creacion de usuario con datos no esperados"""
        url = '/api/v1/pediatras/'
        data = {
                "nombre": "Usuario de Prueba"
                }
        request = self.client.post(url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_specific_pediatrician(self):
        """Verifica que el enpoint para obtener un pediatra por id"""
        url = '/api/v1/pediatras/{}/'.format(self.app_client.id)
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_specific_pediatrician_not_found(self):
        """Verifica que el enpoint para obtener un pediatras por id no encontrado"""
        url = '/api/v1/pediatras/AAA/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_client(self):
        """Verifica que el enpoint para actualizar cliente"""
        url = '/api/v1/pediatras/{}/'.format(self.app_client.id)

        data = {
                "name": "Ernesto"
                }

        request = self.client.patch(url, data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
