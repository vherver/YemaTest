# Django
from django.db import models
from django.core.mail import send_mail
from django.conf import settings

# Python Base
import uuid

# Internos
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient




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
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)

    subject = models.CharField(max_length=50,
                               blank=False,
                               null=True)

    message = models.TextField(blank=False,
                               null=False)

    send_date = models.DateTimeField(auto_now_add=True,
                                     verbose_name="Fecha de Creacion")

    def save(self, *args, **kwargs):

        try:
            message_sended = Mail(
                from_email=settings.FROM_MAIL,
                to_emails=self.destination,
                subject=self.subject,
                html_content=self.message)

            sg = SendGridAPIClient(settings.SENDGRID_KEY)

            sg.send(message_sended)

        except Exception as e:
            print(e)

        super(Mensajes, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'