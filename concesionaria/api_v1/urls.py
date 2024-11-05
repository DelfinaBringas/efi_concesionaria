from rest_framework.routers import DefaultRouter
from api_v1.views.vehiculos import VehiculoViewSet
from api_v1.views.usuario import UserViewSet
from api_v1.views.marca import MarcaViewSet
from api_v1.views.comentarios import ComentariosViewSet

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet, 'vehiculos')
router.register(r'usuario', UserViewSet, 'usuario')
router.register(r'marca', MarcaViewSet, 'marca')
router.register(r'comentarios', ComentariosViewSet,'comentarios')


urlpatterns= router.urls