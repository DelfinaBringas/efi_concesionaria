from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User

from vehiculos.models import (Categoria,Marca,ModeloAuto,Vehiculo,Cliente,Comentario,Venta,ImagenAuto,Usuario)
#CAMBIAR

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen',)

@admin.register(ModeloAuto)
class ModeloAutoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'ano_lanzamiento',)
    list_filter = ('marca', 'ano_lanzamiento',)

@admin.register(Vehiculo)
class AutoAdmin(admin.ModelAdmin):
    ordering = ('modelo', 'precio')
    list_filter = ('marca', 'modelo', 'estado')

    list_display = (
        'marca',
        'modelo',
        'anio',
        'precio',
        'categoria',
        'descripcion',
    )

    fieldsets = [
        (
            "Info del Auto",
            {
                "fields": ["marca", "modelo", "anio", "precio", "categoria", "estado"],
            }
        ),
        (
            "Info Extra",
            {
                "classes": ["collapse"],
                "fields": ["descripcion"]
            }
        )
    ]

    def valor_total(self, obj):
        inventario = Inventario.objects.filter(auto=obj).first()
        if inventario:
            return inventario.cantidad_disponible * obj.precio
        return 0

    def get_stock(self, obj):
        inventario = Inventario.objects.filter(auto=obj).first()
        if inventario:
            stock = inventario.cantidad_disponible
            codigo = "#FF0000"
            if stock >= 500:
                codigo = "#008000"
            elif 10 < stock < 500:
                codigo = "#FFD300"
            return format_html(
                '<span style="color:{};">{}</span>',
                codigo, stock
            )
        return "Sin stock"

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'telefono',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cliente', 'texto', 'fecha',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cliente', 'fecha_venta', 'precio_venta',)
