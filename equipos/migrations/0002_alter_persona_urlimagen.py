# Generated by Django 4.1.2 on 2022-11-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='urlImagen',
            field=models.CharField(default='https://icons.veryicon.com/png/o/internet--web/prejudice/user-128.png', max_length=150),
        ),
    ]
