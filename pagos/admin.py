from django.contrib import admin
from .models import Pago, Webhook

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'metodo', 'monto', 'estado', 'fecha')
    list_filter = ('metodo', 'estado')

@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ('evento', 'pago', 'fecha')
    list_filter = ('evento',)
