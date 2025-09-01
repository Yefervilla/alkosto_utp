from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito_lista, name='carrito_lista'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:linea_id>/', views.eliminar_linea, name='eliminar_linea'),
    path('aplicar-cupon/', views.aplicar_cupon, name='aplicar_cupon'),
]
