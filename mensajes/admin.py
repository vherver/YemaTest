# Django
from django.contrib import admin

# App
from mensajes.models import Mensajes


class MensajeAdmin(admin.ModelAdmin):
    """
    Configuración de campos para administrador Django.
    """
    list_display = ('destination', 'appointment', 'send_date',)

    search_fields = ('destination', 'appointment', 'send_date',)


admin.site.register(Mensajes, MensajeAdmin)


