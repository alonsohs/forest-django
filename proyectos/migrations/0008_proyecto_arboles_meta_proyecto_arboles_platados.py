# Generated by Django 4.1.2 on 2022-11-25 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_alter_proyecto_avance_alter_proyecto_latitud_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='arboles_meta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='arboles_platados',
            field=models.IntegerField(default=0),
        ),
    ]
