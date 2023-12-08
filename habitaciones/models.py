from django.db import models

# Create your models here.
estado_hab=[
    ('Disponible', 'Disponible'),
    ('Ocupada', 'Ocupada'),
    ('Mantenimiento', 'Mantenimiento')
]
tipo_hab=[
    ('Sencilla','Sencilla'),
    ('Doble','Doble'),
    ('Twin','Twin'),
    ('Triple','Triple'),
    ('Familiar','Familiar')
]
class Hab(models.Model):
    codigo=models.CharField(max_length=50, verbose_name="codigo", primary_key=True)
    nro_hab=models.CharField(max_length=50, verbose_name="numero")
    tipo=models.CharField(max_length=50, choices=tipo_hab)
    capacidad=models.IntegerField(verbose_name="capacidad")
    valor=models.FloatField(verbose_name="valor")
    estado=models.CharField(max_length=50, choices=estado_hab)    
    descripcion=models.CharField(max_length=50, verbose_name="descripcion")
    imagen=models.ImageField(upload_to='imagenes/',null=True, verbose_name='imagen')

    def __str__(self):
        fila="Tipo"+self.tipo+"-"+"Estado"+self.estado
        return fila
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()