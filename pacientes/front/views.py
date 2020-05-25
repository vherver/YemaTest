"""
Archivo base para Enpoints de aplicacion
"""

from django.shortcuts import render


def pacientes_view(request):
    if not request.GET.get('page'):
        page = 1
    else:
        page = request.GET.get('page')
    return render(request, 'ListaPacientes.html', {'page': page, 'app': 'pacientes'})