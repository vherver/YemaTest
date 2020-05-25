# Django
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Python Base
import uuid

# Internos


class Citas(models.Model):
    """
        Modelo que representa una cita
    """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          )

    doctor = models.ForeignKey('pediatras.Pediatra',
                               on_delete=models.CASCADE)

    consultorio = models.ForeignKey('consultorio.Consultorio',
                                    on_delete=models.CASCADE)

    patient = models.ForeignKey('pacientes.Paciente',
                                on_delete=models.CASCADE)

    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Fecha de Creacion")

    active = models.BooleanField(default=True,
                                 verbose_name="Activo")

    appointment_date = models.DateTimeField(auto_now_add=True,
                                            verbose_name="Fecha de la Cita")

    def __str__(self):
        return self.patient.full_name() + " - " + self.appointment_date

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
