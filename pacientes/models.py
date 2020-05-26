# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Python Base
import uuid

# Internos


class Paciente(models.Model):
    """
        Modelo que representa los pacientes de la aplicacion
    """

    phone_regex = RegexValidator(
        regex='^\d{9,12}$',
        message=_('Phone number must be entered in the format: 5512345678. Up to 12 digits allowed.')
    )

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
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

    father_name = models.CharField(verbose_name="Nombre del Padre",
                                   max_length=35,
                                   unique=False,
                                   blank=False,
                                   null=True)

    phone = models.CharField(max_length=12,
                             unique=True,
                             validators=[phone_regex, ],
                             verbose_name="Numero de Telefono")

    email = models.EmailField(blank=True,
                              null=True)

    birthdate = models.DateField(blank=True,
                                null=True,
                                verbose_name=_("Fecha de nacimiento"))

    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Fecha de Creacion",
                                         editable=False)

    active = models.BooleanField(default=True,
                                 verbose_name="Activo")

    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default='F',
                              verbose_name="Genero")

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return self.name + " " + self.last_name + " " + self.mother_name
