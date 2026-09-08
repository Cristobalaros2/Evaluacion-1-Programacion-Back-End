from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.lista_productos, name="lista"),
    path("<int:producto_id>/", views.detalle_producto, name="detalle"),
    path("login/", views.vista_login, name="login"),
    path("registro/", views.vista_registro, name="registro"),
    path("logout/", views.vista_logout, name="logout"),
    path("admin/productos/", views.admin_productos, name="admin_productos"),
    path("admin/agregar/", views.admin_agregar, name="admin_agregar"),
    path("admin/editar/<int:producto_id>/", views.admin_editar, name="admin_editar"),
    path("admin/eliminar/<int:producto_id>/", views.admin_eliminar, name="admin_eliminar"),
    path("carrito/", views.ver_carrito, name="carrito"),
    path("carrito/agregar/<int:producto_id>/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path("carrito/actualizar/<int:producto_id>/", views.actualizar_carrito, name="actualizar_carrito"),
    path("carrito/vaciar/", views.vaciar_carrito, name="vaciar_carrito"),
]
