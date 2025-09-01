from django.contrib import admin
from .models import Carrito, LineaCarrito, Cupon

class LineaCarritoInline(admin.TabularInline):
    model = LineaCarrito
    extra = 1

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'fecha_creacion', 'cupon', 'total')
    inlines = [LineaCarritoInline]

@admin.register(Cupon)
class CuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descuento', 'activo')

