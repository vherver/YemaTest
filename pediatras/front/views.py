"""
Archivo base para Enpoints de aplicacion
"""

from django.shortcuts import render


def pediatras_view(request):
    if not request.GET.get('page'):
        page = 1
    else:
        page = request.GET.get('page')
    return render(request, 'ListaPediatras.html', {'page': page, 'app': 'pediatras'})
