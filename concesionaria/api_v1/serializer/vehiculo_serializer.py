from rest_framework import serializers
from vehiculos.models import Marca, Color,Vehiculo, Modelo, Tipo_combustible, Pais_fabricacion

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('nombre', 'pk')

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('nombre', 'pk')

class Tipo_combustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_combustible
        fields = ('nombre', 'pk')

class Pais_fabricacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais_fabricacion
        fields = ('nombre', 'pk')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('nombre', 'pk')

class VehiculoSerializer(serializers.ModelSerializer):
    marca = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all())  
    modelo = serializers.PrimaryKeyRelatedField(queryset=Modelo.objects.all())  
    tipo_combustible = serializers.PrimaryKeyRelatedField(queryset=Tipo_combustible.objects.all())  
    pais_fabricacion = serializers.PrimaryKeyRelatedField(queryset=Pais_fabricacion.objects.all())  
    color = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all())

    class Meta:
        model = Vehiculo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        representation['marca'] = instance.marca.nombre if instance.marca else None
        representation['modelo'] = instance.modelo.nombre if instance.modelo else None
        representation['tipo_combustible'] = instance.tipo_combustible.nombre if instance.tipo_combustible else None
        representation['pais_fabricacion'] = instance.pais_fabricacion.nombre if instance.pais_fabricacion else None
        representation['color'] = instance.color.nombre if instance.color else None
        return representation

    def update(self, instance, validated_data):
        marca_nombre = validated_data.pop('marca', None)
        if marca_nombre:
            try:
                instance.marca = Marca.objects.get(nombre=marca_nombre)
            except Marca.DoesNotExist:
                raise serializers.ValidationError({"marca": "La marca con ese nombre no existe."})

        modelo_nombre = validated_data.pop('modelo', None)
        if modelo_nombre:
            try:
                instance.modelo = Modelo.objects.get(nombre=modelo_nombre)
            except Modelo.DoesNotExist:
                raise serializers.ValidationError({"modelo": "El modelo con ese nombre no existe."})

        tipo_combustible_nombre = validated_data.pop('tipo_combustible', None)
        if tipo_combustible_nombre:
            try:
                instance.tipo_combustible = Tipo_combustible.objects.get(nombre=tipo_combustible_nombre)
            except Tipo_combustible.DoesNotExist:
                raise serializers.ValidationError({"tipo_combustible": "El tipo de combustible con ese nombre no existe."})

        pais_fabricacion_nombre = validated_data.pop('pais_fabricacion', None)
        if pais_fabricacion_nombre:
            try:
                instance.pais_fabricacion = Pais_fabricacion.objects.get(nombre=pais_fabricacion_nombre)
            except Pais_fabricacion.DoesNotExist:
                raise serializers.ValidationError({"pais_fabricacion": "El país de fabricación con ese nombre no existe."})

        color_nombre = validated_data.pop('color', None)
        if color_nombre:
            try:
                instance.color = Color.objects.get(nombre=color_nombre)
            except Color.DoesNotExist:
                raise serializers.ValidationError({"color": "El color con ese nombre no existe."})

        instance.cantidad_puertas = validated_data.get('cantidad_puertas', instance.cantidad_puertas)
        instance.cilindrada = validated_data.get('cilindrada', instance.cilindrada)
        instance.precio_dolares = validated_data.get('precio_dolares', instance.precio_dolares)
        instance.save()
        return instance
