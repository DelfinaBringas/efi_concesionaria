from django.contrib import admin
from .models import Marca, Modelo, Tipo_combustible, Color, Proveedor, Pais_fabricacion, Vehiculo, Comentario, ImagenAuto

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Tipo_combustible)
class TipoCombustibleAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion', 'telefono')

@admin.register(Pais_fabricacion)
class PaisFabricacionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'cantidad_puertas', 'cilindrada', 'tipo_combustible', 'pais_fabricacion', 'precio_dolares', 'color')
    list_filter = ('marca', 'modelo', 'tipo_combustible', 'pais_fabricacion', 'color')
    search_fields = ('marca__nombre', 'modelo__nombre', 'precio_dolares')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'author', 'texto', 'fecha')
    list_filter = ('vehiculo', 'author', 'fecha')
    search_fields = ('texto',)

@admin.register(ImagenAuto)
class ImagenAutoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'description')
    search_fields = ('description',)
    list_filter = ('vehiculo',)
