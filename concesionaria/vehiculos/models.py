from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return  self.nombre
    
class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais_origen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class ModeloAuto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    ano_lanzamiento = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')])
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.anio})'

class Cliente(models.Model):
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre=models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Comentario(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.cliente} sobre {self.auto}'

class Venta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venta de {self.auto} a {self.cliente} el {self.fecha_venta}'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
class Inventario(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    cantidad_disponible = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return f'Inventario de {self.auto} por {self.proveedor} - Cantidad: {self.cantidad_disponible}'

class Vendedor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.usuario.username
    
class ImagenAuto(models.Model):
    auto = models.ForeignKey(
        Auto,
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='images_autos/', null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.description or f'Image of {self.auto}'
    
#FALTA USUARIO: Y ACOMODAR VENDEDOR
class Usuario (models.Model):
    ...