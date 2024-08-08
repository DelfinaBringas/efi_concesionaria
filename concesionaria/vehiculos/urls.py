from django.urls import path
from concesionaria.vehiculos.views.vehiculo_view import(
    vehiculo_list,
    vehiculo_delete,
    vehiculo_create,
    vehiculo_update,
    vehiculo_detail,
    vehiculo_comentarios,
)

urlpatterns = [
    path(route="", view=vehiculo_list, name='vehiculo_lista'),
    path(route="create/", view=vehiculo_create, name='vehiculo_create'),
    path(route="<int:id>/delete/", view=vehiculo_delete, name='vehiculo_delete'),
    path(route="<int:id>/update/", view=vehiculo_update, name='vehiculo_update'),
    path(route="<int:id>/detail/", view=vehiculo_detail, name='vehiculo_detail'),
    path(route="<int:id>/comentarios/", view=vehiculo_comentarios, name='vehiculo_comentarios'),
]
