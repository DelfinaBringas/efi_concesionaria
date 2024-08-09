from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User

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
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True)
    fabricado_el=models.IntegerField(default=datetime.now().year)
    cantidad_puertas = models.IntegerField()
    cilindrada = models.FloatField(default= 0)
    tipo_combustible = models.ForeignKey(Tipo_combustible, on_delete=models.CASCADE, null=True)
    pais_fabricacion = models.ForeignKey(Pais_fabricacion, on_delete=models.CASCADE, null=True)
    precio_dolares = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ${self.precio_dolares}'

class Comentario(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
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
    

