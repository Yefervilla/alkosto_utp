from django.contrib import admin
from pagos.models import Pago, Webhook

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('carrito_id', 'metodo', 'monto', 'estado', 'fecha')
    list_filter = ('metodo', 'estado')
    exclude = ('monto',)

@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    list_display = ('evento', 'pago', 'fecha')
    list_filter = ('evento',)
