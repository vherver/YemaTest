"""
Archivo base para Enpoints de aplicacion
"""

from django.shortcuts import render


def consultorio_view(request):
    if not request.GET.get('page'):
        page = 1
    else:
        page = request.GET.get('page')
    return render(request, 'ListaConsultorios.html', {'page': page, 'app': 'consultorios'})


def consultorio_detail_view(request, consultorio_id):
    if not request.GET.get('page'):
        page = 1
    else:
        page = request.GET.get('page')
    return render(request, 'DetalleConsultorio.html', {'page': page, 'app': 'consultorios', 'consultorio_id': consultorio_id})
