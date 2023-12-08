# Generated by Django 4.2.7 on 2023-11-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0006_habitacion_delete_hab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, verbose_name='codigo')),
                ('tipo', models.CharField(max_length=50, verbose_name='tipo')),
                ('capacidad', models.CharField(max_length=50, verbose_name='capacidad')),
                ('valor', models.CharField(max_length=50, verbose_name='valor')),
            ],
        ),
        migrations.DeleteModel(
            name='Habitacion',
        ),
    ]
