# Django
from django.contrib import admin

# App
from consultorio.models import Consultorio


class ConsultorioAdmin(admin.ModelAdmin):
    """
    Configuración de campos para administrador Django.
    """
    list_display = ('hospital', 'office', 'creation_date', 'active')

    search_fields = ('hospital', 'office', 'creation_date',)

    list_filter = ('active', )


admin.site.register(Consultorio, ConsultorioAdmin)


