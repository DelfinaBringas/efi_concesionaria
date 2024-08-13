from django.urls import path
from vehiculos.views.vehiculo_view import (
    VehiculoCreateView,
    VehiculoDeleteView,
    VehiculoDetailView,
    VehiculoUpdateView,
    VehiculoListView,
)

from vehiculos.views.proveedor_view import (
    ProveedorCreateView,
    ProveedorDeleteView,
    ProveedorDetailView,
    ProveedorUpdateView,
    ProveedorListView,
)

from vehiculos.views.comentario_view import (
    ComentarioCreateView,
    ComentarioDeleteView,
    ComentarioDetailView,
    ComentarioListView,
    ComentarioUpdateView
)

urlpatterns = [
    path(route="", view=VehiculoListView.as_view(), name='vehiculo_list'),
    path(route="create/", view=VehiculoCreateView.as_view(), name='vehiculo_create'),
    path(route="<int:id>/delete/", view=VehiculoDeleteView.as_view(), name='vehiculo_delete'),
    path(route="<int:id>/update/", view=VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path(route="<int:id>/detail/", view=VehiculoDetailView.as_view(), name='vehiculo_detail'),

    path(route='proveedor/', view=ProveedorListView.as_view(), name='proveedor_list'),
    path(route='proveedor/<int:id>/delete/', view=ProveedorDeleteView.as_view(), name="proveedor_delete"),
    path(route='proveedor/create/', view=ProveedorCreateView.as_view(), name='proveedor_create'),
    path(route='proveedor/<int:id>/', view=ProveedorDetailView.as_view(), name="proveedor_detail"),
    path(route='proveedor/<int:id>/update/', view=ProveedorUpdateView.as_view(), name="proveedor_update"),

    path('comentario/<int:vehiculo_id>/', view=ComentarioListView.as_view(), name='comentario_list'),
    path('comentario/<int:id>/delete/', view=ComentarioDeleteView.as_view(), name='comentario_delete'),
    path('comentario/create/<int:vehiculo_id>/', view=ComentarioCreateView.as_view(), name='comentario_create'),
    path(route='comentario/<int:id>/', view=ComentarioDetailView.as_view(), name="comentario_detail"),
    path(route='comentario/<int:id>/update/', view=ComentarioUpdateView.as_view(), name="comentario_update"),

]
