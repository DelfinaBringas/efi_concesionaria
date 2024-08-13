
from vehiculos.models import Comentario

def recent_comments(request):
    comments = Comentario.objects.order_by('-fecha')[:5]  # Últimos 5 comentarios
    return {
        'recent_comments': comments
    }
