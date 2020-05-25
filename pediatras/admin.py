# Django
from django.contrib import admin

# App
from pediatras.models import Pediatra


class PediatraAdmin(admin.ModelAdmin):
    """
    Configuración de campos para administrador Django.
    """
    list_display = ('name', 'last_name', 'mother_name', 'active', 'phone',)

    search_fields = ('name', 'last_name', 'mother_name', 'phone')

    list_filter = ('active', )


admin.site.register(Pediatra, PediatraAdmin)


