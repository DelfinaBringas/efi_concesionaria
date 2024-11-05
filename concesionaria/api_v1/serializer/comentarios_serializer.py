from rest_framework import serializers
from vehiculos.models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    vehiculo_id = serializers.IntegerField(source='vehiculo.id', read_only=True)
    vehiculo_marca = serializers.CharField(source='vehiculo.marca.nombre', read_only=True)
    vehiculo_modelo = serializers.CharField(source='vehiculo.modelo.nombre', read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'vehiculo_id', 'vehiculo_marca', 'vehiculo_modelo', 'author', 'texto', 'fecha']
