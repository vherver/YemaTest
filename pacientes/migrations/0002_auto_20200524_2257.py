# Generated by Django 3.0.6 on 2020-05-25 03:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='creation_date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='father_name',
            field=models.CharField(max_length=35, null=True, verbose_name='Nombre del Padre'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='last_name',
            field=models.CharField(max_length=35, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='mother_name',
            field=models.CharField(max_length=35, null=True, verbose_name='Apellido Materno'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='name',
            field=models.CharField(max_length=35, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='phone',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 5512345678. Up to 12 digits allowed.', regex='^\\d{9,12}$')], verbose_name='Numero de Telefono'),
        ),
    ]