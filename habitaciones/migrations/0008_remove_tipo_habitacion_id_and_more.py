# Generated by Django 4.2.7 on 2023-11-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitaciones', '0007_tipo_habitacion_delete_habitacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_habitacion',
            name='id',
        ),
        migrations.AlterField(
            model_name='tipo_habitacion',
            name='codigo',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='codigo'),
        ),
    ]
