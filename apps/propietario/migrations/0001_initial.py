# Generated by Django 4.2.1 on 2023-06-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario_is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('propietario_nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('propietario_barberia', models.CharField(max_length=255, verbose_name='Barberia')),
                ('propietario_ciut', models.IntegerField(blank=True, null=True, verbose_name='Cuit')),
            ],
        ),
    ]
