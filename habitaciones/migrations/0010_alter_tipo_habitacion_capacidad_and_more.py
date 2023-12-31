# Generated by Django 4.2.7 on 2023-11-19 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0009_alter_tipo_habitacion_capacidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_habitacion',
            name='capacidad',
            field=models.IntegerField(verbose_name='capacidad'),
        ),
        migrations.AlterField(
            model_name='tipo_habitacion',
            name='valor',
            field=models.FloatField(verbose_name='valor'),
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('nro_hab', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='numero')),
                ('estado', models.CharField(max_length=50, verbose_name='estado')),
                ('descripcion', models.CharField(max_length=50, verbose_name='descripcion')),
                ('codigoTipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habitaciones.tipo_habitacion')),
            ],
        ),
    ]
