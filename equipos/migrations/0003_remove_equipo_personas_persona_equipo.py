# Generated by Django 4.1.3 on 2022-11-24 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0002_alter_persona_urlimagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='personas',
        ),
        migrations.AddField(
            model_name='persona',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipos.equipo'),
        ),
    ]
