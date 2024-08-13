from typing import List
from typing import List, Optional
from django.contrib.auth.models import User
from vehiculos.models import Comentario, Vehiculo
from vehiculos.repositories.vehiculo import VehiculoRepository

class ComentarioRepository:

    def get_all(self) -> List[Comentario]:
        return Comentario.objects.all()
    
    def get_by_id(self, id:int) -> Optional[Comentario]:
        return Comentario.objects.get(id=id)
    
    def delete(self, comentario:Comentario):
        comentario.delete()
    
    def create(
        self,
        vehiculo_id: int,
        author: User,
        texto: str
    ) -> Comentario:
        vehiculo_repo = VehiculoRepository()
        vehiculo = vehiculo_repo.get_by_id(vehiculo_id)
        review=Comentario.objects.create(
            vehiculo=vehiculo,
            author=author,
            texto=texto
        )
        return review
        # try:
        #     vehiculo = Vehiculo.objects.get(id=vehiculo_id)
        # except Vehiculo.DoesNotExist:
        #     raise ValueError("Vehículo no encontrado")

        # comentario = Comentario.objects.create(
        #     vehiculo=vehiculo,
        #     author=author,
        #     texto=texto
        # )
        # return comentario
    
    def update(
        self, 
        comentario: Comentario,
        vehiculo:str,
        author:str,
        texto:str,
        ):
          comentario.vehiculo=vehiculo
          comentario.author=author
          comentario.texto=texto
          comentario.save()