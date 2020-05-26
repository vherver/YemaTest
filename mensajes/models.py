# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Python Base
import uuid

# Internos


class Mensajes(models.Model):
    """
        Modelo que representa los pacientes de la aplicacion
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          )

    destination = models.EmailField(blank=None,
                                    null=False)

    appointment = models.ForeignKey('citas.Citas',
                                    on_delete=models.CASCADE)

    message = models.TextField(editable=False)

    send_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Fecha de Creacion")

    def save(self, *args, **kwargs):

        # Aqui se enviara correo electronico para confirmar cita
        super(Mensajes, self).save(*args, **kwargs)
