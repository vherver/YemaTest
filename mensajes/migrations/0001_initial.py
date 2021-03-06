# Generated by Django 3.0.6 on 2020-05-26 04:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('citas', '0003_citas_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('destination', models.EmailField(blank=None, max_length=254)),
                ('message', models.TextField(editable=False)),
                ('send_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='citas.Citas')),
            ],
        ),
    ]
