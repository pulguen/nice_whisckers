# Generated by Django 4.2.1 on 2023-06-20 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barberia', '0002_barberia_propietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barberia',
            name='propietario',
        ),
    ]