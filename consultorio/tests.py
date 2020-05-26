from rest_framework.test import APITestCase
from rest_framework import status

from consultorio.models import Consultorio


class ConsultorioAPITestCase(APITestCase):
    """Test para creacion de pacientes"""

    def setUp(self):
        self.app_client = Consultorio.objects.create(
            hospital="Hospital 1",
            office="305-A"
        )

    def test_office_list(self):
        """Verifica que el enpoint de obtencion de lista de consultorios responda con 200"""
        url = '/api/v1/consultorios/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_office_creation(self):
        """Verifica que el enpoint de creacion de consultorios funcione correctamente"""
        url = '/api/v1/consultorios/'
        data = {
                    "hospital": "Angeles Roma",
                    "office": "306"
                }
        request = self.client.post(url, data)

        self.assertEqual(request.status_code, status.HTTP_201_CREATED)


    def test_office_bad_request(self):
        """Verifica que el enpoint de creacion de consultorios con datos no esperados"""
        url = '/api/v1/consultorios/'
        data = {
                "nombre": "Usuario de Prueba"
                }
        request = self.client.post(url, data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_specific_office(self):
        """Verifica que el enpoint para obtener un consultorios por id"""
        url = '/api/v1/consultorios/{}/'.format(self.app_client.id)
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_get_specific_office_not_found(self):
        """Verifica que el enpoint para obtener un consultorios por id no encontrado"""
        url = '/api/v1/consultorios/AAA/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_office(self):
        """Verifica que el enpoint para actualizar consultorios"""
        url = '/api/v1/consultorios/{}/'.format(self.app_client.id)

        data = {
                "hospital": "Hospital 2"
                }

        request = self.client.patch(url, data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
