# Generated by Django 3.1.2 on 2020-11-03 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_auto_20201103_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='year',
            field=models.FloatField(null=True),
        ),
    ]
