# Generated by Django 5.0.7 on 2024-08-16 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0002_vehiculo_fabricado_el'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
