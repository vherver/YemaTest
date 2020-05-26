# Django
from django.db import models
from django.conf import settings

# Python Base
import uuid

# Internos
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient


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
                                         verbose_name="Fecha de Creacion",
                                         editable=False)

    active = models.BooleanField(default=True,
                                 verbose_name="Activo")

    appointment_date = models.DateTimeField(verbose_name="Fecha de la Cita",)

    comment = models.TextField()

    def __str__(self):
        return self.patient.full_name() + " - " + self.appointment_date.strftime("%d - %B - %Y, %H:%M:%S" )

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'

    @property
    def get_appointmentt_str_date(self):
        return self.appointment_date.strftime("%d - %B - %Y, %H:%M:%S")


    def save(self, *args, **kwargs):

        try:
            if self.patient.email:
                message = '<div class=\"card w-25\">' \
                          '  <div class=\"card-header\">' \
                          '        <h1>Confirmación de Cita</h3>' \
                          '    </div>' \
                          '   <div class=\"card-body\">' \
                          '        Estimado usuario, este correo electronico es para confirmar la cita que ' \
                          '        se le agendo en  nuestra plataforma ' \
                          '        <h3 class=\"card-title\">Identificador de cita: {}</h3> ' \
                          '        <h3 class=\"card-text\">Paciente: {}</p>' \
                          '        <h3 class=\"card-text\">Pediatra: {}</p>' \
                          '        <h3 class=\"card-text\">Fecha y Hora: {}</p>' \
                          '        <h3 class=\"card-text\">Consultorio: {}</p>' \
                          '        <h3 class=\"card-text\">Comentarios: {}</p>' \
                          '    </div>' \
                          '    Saludos.<br>    ' \
                          'Plataforma Yema - Victor Herver' \
                          '</div>'.format(self.id, self.patient.full_name(), self.doctor.full_name(),
                                          self.appointment_date, self.consultorio, self.comment)

                message_sended = Mail(
                    from_email=settings.FROM_MAIL,
                    to_emails=self.patient.email,
                    subject="Confirmación de Cita",
                    html_content=message)

                sg = SendGridAPIClient(settings.SENDGRID_KEY)

                sg.send(message_sended)

        except Exception as e:
            print(e)

        super(Citas, self).save(*args, **kwargs)

