# Generated by Django 4.1.2 on 2022-11-25 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_proyecto_urlimagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_limite',
            field=models.DateTimeField(),
        ),
    ]