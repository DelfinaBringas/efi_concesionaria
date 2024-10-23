# from rest_framework import serializers
# from vehiculos.models import Vehiculo, Comentario, Color, Pais_fabricacion, Tipo_combustible, Marca


# # COMENTARIO:
# class ComentarioSerializer(serializers.ModelSerializer):
#     texto = serializers.SerializerMethodField()

#     class Meta:
#         model = Comentario
#         fields = '__all__'

#     def get_texto(self, comentario):
#         if not comentario.texto:
#             return "No posee comentarios"
#         return comentario.texto

#     def update(self, instance, validated_data):
#         vehiculo_data = validated_data.pop('vehiculo', None)
#         if vehiculo_data:
#             vehiculo, _ = Vehiculo.objects.get_or_create(**vehiculo_data)
#             instance.vehiculo = vehiculo  

#         instance.author = validated_data.get('author', instance.author)
#         instance.texto = validated_data.get('texto', instance.texto)
#         instance.fecha = validated_data.get('fecha', instance.fecha)

#         instance.save()
#         return instance

# # VEHICULO:
# class VehiculoSerializer(serializers.ModelSerializer):
#     comentarios = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = Vehiculo
#         fields = '__all__'

#     def get_comentarios(self, vehiculo):
#         comentarios = vehiculo.comentarios.all()
#         if not comentarios:
#             return [{"texto": "No posee comentarios"}]
#         # Si hay comentarios, los serializamos usando ComentarioSerializer
#         return ComentarioSerializer(comentarios, many=True).data

from rest_framework import serializers
from vehiculos.models import Vehiculo, Comentario, Color, Pais_fabricacion, Tipo_combustible, Marca

# COMENTARIO:
class ComentarioSerializer(serializers.ModelSerializer):
    texto = serializers.SerializerMethodField()

    class Meta:
        model = Comentario
        fields = ['id', 'author', 'texto', 'fecha']  # Ajusta los campos según tu modelo

    def get_texto(self, comentario):
        if not comentario.texto:
            return "No posee comentarios"
        return comentario.texto

    def update(self, instance, validated_data):
        vehiculo_data = validated_data.pop('vehiculo', None)
        if vehiculo_data:
            vehiculo, _ = Vehiculo.objects.get_or_create(**vehiculo_data)
            instance.vehiculo = vehiculo  

        instance.author = validated_data.get('author', instance.author)
        instance.texto = validated_data.get('texto', instance.texto)
        instance.fecha = validated_data.get('fecha', instance.fecha)

        instance.save()
        return instance


# VEHICULO:
class VehiculoSerializer(serializers.ModelSerializer):
    comentarios = serializers.SerializerMethodField()

    class Meta:
        model = Vehiculo
        fields = '__all__'

    def get_comentarios(self, vehiculo):
        comentarios = vehiculo.comentarios.all()
        if not comentarios:
            return [{"texto": "No posee comentarios"}]  # Mensaje si no hay comentarios

        # Si hay comentarios, los serializamos usando ComentarioSerializer
        return ComentarioSerializer(comentarios, many=True).data

    # def update(self, instance, validated_data):
    #     # Extraer los datos de los comentarios
    #     comentarios_data = validated_data.pop('comentarios', None)

    #     # Actualizar los campos del vehículo
    #     instance.marca = vatdated_data.get('marca', instance.marca)
    #     instance.modelo = validated_data.get('modelo', instance.modelo)
    #     instance.cantidad_puertas = validated_data.get('cantidad_puertas', instance.cantidad_puertas)
    #     instance.cilindrada = validated_data.get('cilindrada', instance.cilindrada)
    #     instance.precio_dolares = validated_data.get('precio_dolares', instance.precio_dolares)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.pais_fabricacion = validated_data.get('pais_fabricacion', instance.pais_fabricacion)
    #     instance.tipo_combustible = validated_data.get('tipo_combustible', instance.tipo_combustible)

    #     # Guardar la instancia del vehículo
    #     instance.save()

    #     if comentarios_data:
    #         # Opcional: puedes decidir mantener los comentarios existentes
    #         # instance.comentarios.all().delete()  # Eliminar comentarios existentes
    #         for comentario_data in comentarios_data:
    #             # Aquí puedes decidir si quieres actualizar o crear nuevos comentarios
    #             comentario_id = comentario_data.get('id', None)
    #             if comentario_id:  # Si existe un ID, actualiza el comentario
    #                 comentario = Comentario.objects.get(id=comentario_id)
    #                 comentario.texto = comentario_data.get('texto', comentario.texto)
    #                 comentario.save()
    #             else:  # Si no existe un ID, crea un nuevo comentario
    #                 Comentario.objects.create(vehiculo=instance, **comentario_data)

    #     return instance

   