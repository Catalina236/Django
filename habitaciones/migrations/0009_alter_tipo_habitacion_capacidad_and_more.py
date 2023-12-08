# Generated by Django 4.2.7 on 2023-11-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0008_remove_tipo_habitacion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_habitacion',
            name='capacidad',
            field=models.IntegerField(max_length=50, verbose_name='capacidad'),
        ),
        migrations.AlterField(
            model_name='tipo_habitacion',
            name='valor',
            field=models.FloatField(max_length=50, verbose_name='valor'),
        ),
    ]