# Generated by Django 4.0.4 on 2022-05-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamilia', '0005_equipo_imagen1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='imagen1',
            field=models.ImageField(null=True, upload_to='equipos'),
        ),
    ]
