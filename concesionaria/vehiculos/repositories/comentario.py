from typing import List, Optional
from vehiculos.models import Comentario,Vehiculo

class ComentarioRepository:
    def get_all(self) -> List[Comentario]:
        return Comentario.objects.all()
    
    def get_by_id(self,id:int) -> Optional [Comentario]:
        try:
            return Comentario.objects.get(id=id)
        except Comentario.DoesNotExist:
            return None
        
    def create( 
            self,
            vehiculo:Optional[Vehiculo],
            author:str,
            texto:str,
    ) -> Comentario:
        return Comentario.objects.create(
            author=author,
            vehiculo=vehiculo,
            texto=texto,
        )
    
    def delete(self, comentario: Comentario):
        return comentario.delete()
    
    def update(
            self,
            vehiculo:Optional[Vehiculo],
            author: str,
            texto:str,
    ) -> Comentario:
        Comentario.vehiculo= vehiculo
        Comentario.author=author
        Comentario.texto=texto
