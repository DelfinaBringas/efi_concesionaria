import django_filters

from vehiculos.models import Vehiculo

class VehiculoFilter(django_filters.FilterSet):
    marca = django_filters.CharFilter(
        field_name='marca_id',
        lookup_expr='exact'
    )
    min_price = django_filters.NumberFilter(
        field_name='precio_dolares',  
        lookup_expr='gte'  
    )
    max_price = django_filters.NumberFilter(
        field_name='precio_dolares', 
        lookup_expr='lte' 
    )

    class Meta:
        model = Vehiculo
        fields= ['marca','min_price', 'max_price']