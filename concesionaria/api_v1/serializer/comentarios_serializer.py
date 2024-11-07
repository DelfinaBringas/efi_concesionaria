from rest_framework import serializers
from vehiculos.models import Comentario, Vehiculo, User

class ComentarioSerializer(serializers.ModelSerializer):
    vehiculo = serializers.PrimaryKeyRelatedField(queryset=Vehiculo.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Comentario
        fields = ['vehiculo', 'author', 'texto', 'fecha']