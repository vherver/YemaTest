# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Python Base
import uuid

# Internos


class Pediatra(models.Model):
    """
        Modelo que representa a un pediatra de la aplicacion
    """

    phone_regex = RegexValidator(
        regex='^\d{9,12}$',
        message=_('El formato correcto para es: 5512345678. Hasta 12 digitos.')
    )

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          )

    name = models.CharField(verbose_name="Nombre",
                            max_length=35,
                            unique=False,
                            blank=False)

    last_name = models.CharField(verbose_name="Apellido",
                                 max_length=35,
                                 unique=False,
                                 blank=False)

    mother_name = models.CharField(verbose_name="Apellido Materno",
                                   max_length=35,
                                   unique=False,
                                   blank=False,
                                   null=True)

    phone = models.CharField(max_length=12,
                             unique=True,
                             validators=[phone_regex, ],
                             verbose_name="Numero de Telefono")

    mail = models.EmailField()

    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Fecha de creacion")

    active = models.BooleanField(default=True,
                                 verbose_name="Activo")

    def __str__(self):
        return self.name
