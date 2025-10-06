from django.contrib import admin
from .models import Producto, Categoria , Rating

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion","precio", "stock")
    search_fields = ("nombre",)
    list_filter = ("categoria",)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "parend_id")
    list_filter = ("parend_id",)
    search_fields = ("nombre","parend_id__nombre")

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "producto", "valor")
    search_fields = ("user__username", "producto__nombre")
    list_filter = ("valor", "producto")


admin.site.site_header = "Administración de Alkosto"
admin.site.site_title = "Alkosto Admin"
admin.site.index_title = "Panel de Administración"