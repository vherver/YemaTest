# Django
from django.db import models
from django.core.validators import RegexValidator


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

    name = models.CharField(verbose_name="Name",
                            max_length=35,
                            unique=False,
                            blank=False)

    last_name = models.CharField(verbose_name="Last Name",
                                 max_length=35,
                                 unique=False,
                                 blank=False)

    mother_name = models.CharField(verbose_name="Mother Name",
                                   max_length=35,
                                   unique=False,
                                   blank=False,
                                   null=True)

    father_name = models.CharField(verbose_name="Responsible Name",
                                   max_length=35,
                                   unique=False,
                                   blank=False,
                                   null=True)

    phone = models.CharField(max_length=12,
                             unique=True,
                             validators=[phone_regex, ],
                             verbose_name="Phone Number")

    birthdate = models.DateField(blank=True,
                                null=True,
                                verbose_name=_("Birthdate"))

    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name="Created")

    active = models.BooleanField(default=True,
                                 verbose_name="Active")

    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default='F',
                              verbose_name="Gender")

    def __str__(self):
        return self.name
