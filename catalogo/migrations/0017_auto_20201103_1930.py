# Generated by Django 3.1.2 on 2020-11-03 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0016_auto_20201103_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='Año',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='Precio',
        ),
    ]
