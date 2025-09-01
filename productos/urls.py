from django.urls import path
from . import views

urlpatterns = [
    path("productos/", views.lista_productos, name="lista_productos"),
    path("productos/nuevo/", views.crear_producto, name="crear_producto"),
    path('', views.lista_productos, name='productos_lista'),

]