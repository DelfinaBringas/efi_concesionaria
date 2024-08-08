from typing import List, Optional
from vehiculos.models import Color

class ColorRepository:
    def get_all(self) -> List[Color]:
        return Color.objects.all()
        
    def get_by_id(self, id: int) -> Optional[Color]:
        try:
            return Color.objects.get(id=id)
        except Color.DoesNotExist:
            return None

    def create(
        self,
        nombre: str,
    ) -> Color:
        return Color.objects.create(
            nombre=nombre,
        )
    
    def delete(self, color: Color):
        return color.delete()
    
    def update(
        self,
        color: Color,
        nombre: str,
    ) -> Color:
        color.nombre = nombre
        color.save()
        return color