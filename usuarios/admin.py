from django.contrib import admin
from usuarios.models import Favorito
# Register your models here.


@admin.register(Favorito)
class FavoritosAdmin(admin.ModelAdmin):
    list_display = ("user", "producto")
    search_fields = ("user__username", "producto__nombre")
    list_filter = ("user",)
