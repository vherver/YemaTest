# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Python Base
import uuid

# Internos


class Consultorio(models.Model):
    """
        Modelo que representa los consultorios de la aplicacion
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          )


    hospital = models.CharField(verbose_name="Hospital",
                            max_length=35,
                            unique=False,
                            blank=False)

    office = models.CharField(verbose_name="Consultorio",
                              max_length=35,
                              unique=False,
                              blank=False)

    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Fecha de Creacion")

    active = models.BooleanField(default=True,
                                 verbose_name="Activo")

    def __str__(self):
        return self.hospital + " " + self.office

    @property
    def get_full_name(self):
        return self.hospital + " " + self.office

