from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from vehiculos.manager import ProductQuerySet

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return  self.nombre
    
class Tipo_combustible(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return  self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Pais_fabricacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca, related_name='vehiculos',on_delete=models.CASCADE,verbose_name=_('Marca'))
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, verbose_name=_('Modelo'))
    fabricado_el=models.IntegerField(default=datetime.now().year, verbose_name=_('Año de Fabricación'))
    cantidad_puertas = models.IntegerField(verbose_name=_('Cantidad de Puertas'))
    cilindrada = models.FloatField(default= 0,  verbose_name=_('Cilindrada'))
    tipo_combustible = models.ForeignKey(Tipo_combustible, on_delete=models.CASCADE, null=True,   verbose_name=_('Tipo de Combustible'))
    pais_fabricacion = models.ForeignKey(Pais_fabricacion, on_delete=models.CASCADE, null=True, verbose_name=_('País de Fabricación'))
    precio_dolares = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name=_('Precio en USD'))
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True,  verbose_name=_('Color'))
    active=models.BooleanField(default=True,  verbose_name=_('Activo'))
    
    objects = ProductQuerySet.as_manager()

    def __str__(self):
        return f'{self.marca} {self.modelo} ${self.precio_dolares}'

class Comentario(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE,related_name='comentarios')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.author} sobre {self.vehiculo}'

class ImagenAuto(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo,
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='images_vehiculo/', null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f'Image of {self.vehiculo}'
    

