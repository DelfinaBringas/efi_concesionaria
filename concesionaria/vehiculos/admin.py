from django.contrib import admin
from django.utils.html import format_html
from vehiculos.models import (Categoria,Marca,ModeloAuto,Auto,Cliente,Comentario,Venta,Proveedor,Inventario,Vendedor,ImagenAuto,Usuario)
#FALTAN LOS UNTIMOS 3 PORQUE NOSE SI ESTAN BIEN

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen',)
    search_fields = ('nombre', 'pais_origen',)

@admin.register(ModeloAuto)
class ModeloAutoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'ano_lanzamiento',)
    search_fields = ('nombre', 'marca__nombre',)
    list_filter = ('marca', 'ano_lanzamiento',)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    ordering = ('modelo', 'precio')
    search_fields = ('precio', 'modelo__nombre', 'marca__nombre',)
    list_filter = ('marca', 'modelo', 'estado',)
    empty_value_display = "No hay datos para este campo"
    readonly_fields = ("modelo",)

    list_display = (
        'modelo',
        'precio',
        'categoria',
        'estado',
        'descripcion',
        'get_stock',
        'valor_total',
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
    search_fields = ('nombre', 'apellido', 'telefono',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cliente', 'texto', 'fecha',)
    search_fields = ('auto__modelo__nombre', 'cliente__nombre', 'texto',)
    list_filter = ('fecha', 'auto', 'cliente',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cliente', 'fecha_venta', 'precio_venta',)
    search_fields = ('auto__modelo__nombre', 'cliente__nombre', 'precio_venta',)
    list_filter = ('fecha_venta', 'auto', 'cliente',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono',)
    search_fields = ('nombre', 'telefono',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('auto', 'cantidad_disponible', 'proveedor',)
    search_fields = ('auto__modelo__nombre', 'proveedor__nombre',)
    list_filter = ('auto', 'proveedor',)