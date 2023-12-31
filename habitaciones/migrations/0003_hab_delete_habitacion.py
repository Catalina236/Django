# Generated by Django 4.2.7 on 2023-11-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0002_remove_habitacion_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_hab', models.CharField(max_length=50, verbose_name='numero')),
                ('codigo', models.CharField(max_length=50, verbose_name='codigo')),
                ('estado', models.PositiveIntegerField(verbose_name='estado')),
                ('descripcion', models.FloatField(max_length=50, verbose_name='descripcion')),
            ],
        ),
        migrations.DeleteModel(
            name='Habitacion',
        ),
    ]
