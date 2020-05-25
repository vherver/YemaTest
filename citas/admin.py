# Django
from django.contrib import admin

# App
from citas.models import Citas


class CitaAdmin(admin.ModelAdmin):
    """
    Configuración de campos para administrador Django.
    """
    list_display = ('doctor', 'consultorio', 'patient', 'creation_date', 'appointment_date',)

    search_fields = ('doctor', 'consultorio', 'patient',)

    list_filter = ('active', )


admin.site.register(Citas, CitaAdmin)


