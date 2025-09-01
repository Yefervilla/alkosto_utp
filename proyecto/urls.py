from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("usuarios.urls")),
    path("productos/", include("productos.urls")),
    path('pagos/', include('pagos.urls')),
    path('carrito/', include('carrito.urls')),
]
