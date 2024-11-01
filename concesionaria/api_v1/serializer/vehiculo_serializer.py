from rest_framework import serializers
from vehiculos.models import Vehiculo, Comentario, Marca

# MARCA:
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('nombre', 'pk')

# COMENTARIO:
class ComentarioSerializer(serializers.ModelSerializer):
    author_nombre = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comentario
        fields = ['id', 'vehiculo', 'author', 'author_nombre', 'texto', 'fecha']

# VEHICULO:
class VehiculoSerializer(serializers.ModelSerializer):
    # Mantener la selección de marca como PK para el formulario
    marca = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all())
    comentarios = ComentarioSerializer(many=True, read_only=True)
    active = serializers.BooleanField(default=True) 

    class Meta:
        model = Vehiculo
        fields = [
            'marca', 'modelo', 'fabricado_el', 'cantidad_puertas', 'cilindrada',
            'tipo_combustible', 'pais_fabricacion', 'precio_dolares', 
            'color', 'active', 'comentarios'
        ]

    def to_representation(self, instance):
        # Anidar el serializador de Marca solo en la respuesta
        representation = super().to_representation(instance)
        representation['marca'] = MarcaSerializer(instance.marca).data
        return representation

    def create(self, validated_data):
        # Extraer datos de la marca
        marca_data = validated_data.pop('marca')
        marca, _ = Marca.objects.get_or_create(pk=marca_data)
        validated_data['marca'] = marca

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Actualiza el campo de marca
        marca_data = validated_data.pop('marca', None)
        if marca_data:
            instance.marca = Marca.objects.get(pk=marca_data)
        
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.fabricado_el = validated_data.get('fabricado_el', instance.fabricado_el)
        instance.cantidad_puertas = validated_data.get('cantidad_puertas', instance.cantidad_puertas)
        instance.cilindrada = validated_data.get('cilindrada', instance.cilindrada)
        instance.tipo_combustible = validated_data.get('tipo_combustible', instance.tipo_combustible)
        instance.pais_fabricacion = validated_data.get('pais_fabricacion', instance.pais_fabricacion)
        instance.precio_dolares = validated_data.get('precio_dolares', instance.precio_dolares)
        instance.color = validated_data.get('color', instance.color)
        instance.active = validated_data.get('active', instance.active)

        instance.save()
        return instance
