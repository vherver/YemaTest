"""YemaTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/v1/pacientes/', include('pacientes.api_v1.urls', namespace='pacientes')),
    path(r'api/v1/pediatras/', include('pediatras.api_v1.urls', namespace='pediatras')),
    path(r'api/v1/consultorios/', include('consultorio.api_v1.urls', namespace='consultorios')),
    path(r'api/v1/citas/', include('citas.api_v1.urls', namespace='citas')),
]

admin.site.site_header = 'Yema Test - Victor Herver'

