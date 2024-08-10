from django.urls import path
from vehiculos.views.vehiculo_view import(
    vehiculo_list,
    vehiculo_delete,
    vehiculo_create,
    vehiculo_update,
    vehiculo_detail,
)

from vehiculos.views.proveedor_view import(
    proveedor_list,
    proveedor_delete,
    proveedor_create,
    proveedor_detail,
    proveedor_update,
)

from vehiculos.views.comentario_view import(
    comentario_list,
    comentario_delete,
    comentario_create,
    comentario_detail,
    comentario_update,
    
)

urlpatterns = [
    path(route="", view=vehiculo_list, name='vehiculo_list'),
    path(route="create/", view=vehiculo_create, name='vehiculo_create'),
    path(route="<int:id>/delete/", view=vehiculo_delete, name='vehiculo_delete'),
    path(route="<int:id>/update/", view=vehiculo_update, name='vehiculo_update'),
    path(route="<int:id>/detail/", view=vehiculo_detail, name='vehiculo_detail'),

    path(route='proveedor/', view=proveedor_list, name='proveedor_list'),
    path(route='proveedor/<int:id>/delete/',view=proveedor_delete,name="proveedor_delete"),
    path(route='proveedor/create/',view=proveedor_create, name='proveedor_create'),
    path(route='proveedor/<int:id>/',view=proveedor_detail,name="proveedor_detail"),
    path(route='proveedor/<int:id>/update/',view=proveedor_update,name="proveedor_update"),

    path(route='comentario/', view=comentario_list, name='comentario_list'),
    path(route='comentario/<int:id>/delete/',view=comentario_delete,name="comentario_delete"),
    path(route='comentario/create/',view=comentario_create, name='comentario_create'),
    path(route='comentario/<int:id>/',view=comentario_detail,name="comentario_detail"),
    path(route='comentario/<int:id>/update/',view=comentario_update,name="comentario_update"),

    
]
