# Generated by Django 3.0.6 on 2020-05-24 20:15

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=35, verbose_name='Name')),
                ('last_name', models.CharField(max_length=35, verbose_name='Last Name')),
                ('mother_name', models.CharField(max_length=35, null=True, verbose_name='Mother Name')),
                ('father_name', models.CharField(max_length=35, null=True, verbose_name='Responsible Name')),
                ('phone', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 5512345678. Up to 12 digits allowed.', regex='^\\d{9,12}$')], verbose_name='Phone Number')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1, verbose_name='Gender')),
            ],
        ),
    ]