"""
Archivo base para Enpoints de aplicacion
"""

from django.shortcuts import render


def citas_view(request):
    if not request.GET.get('page'):
        page = 1
    else:
        page = request.GET.get('page')
    return render(request, 'ListaCitas.html', {'page': page, 'app': 'citas'})
