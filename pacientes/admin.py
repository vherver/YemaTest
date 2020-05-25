# Django
from django.contrib import admin

# App
from pacientes.models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    """
    Configuración de campos para administrador Django.
    """
    list_display = ('name', 'last_name', 'mother_name', 'active', 'phone', 'gender', 'birthdate')

    search_fields = ('name', 'last_name', 'mother_name', 'phone')

    list_filter = ('active', )


admin.site.register(Paciente, PacienteAdmin)


