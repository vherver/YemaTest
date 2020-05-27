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


def pacientes_detail_view(request, paciente_id):
    if not request.GET.get('page'):
        page = 1
    else:
        page = request.GET.get('page')
    return render(request, 'DetallePacientes.html', {'page': page, 'app': 'pacientes', 'paciente_id': paciente_id})
