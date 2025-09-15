from django.db import models
from carrito.models import Carrito
class Pago(models.Model):
    METODOS = [
        ('MP', 'Mercado Pago'),
        ('PU', 'PayU Latam'),
        ('ST', 'Stripe'),
    ]
    ESTADOS = [
        ('pe', 'Pendiente'),
        ('ap', 'Aprobado'),
        ('re', 'Rechazado'),
    ]
    
    metodo = models.CharField(max_length=2, choices=METODOS)
    carrito_id = models.ForeignKey(Carrito, null=False, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=2, choices=ESTADOS)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carrito_id.user.username + " - " + self.metodo
    
    def save(self, *args, **kwargs):
        if self.carrito_id:
            self.monto = self.carrito_id.total
        super().save(*args, **kwargs)

class Webhook(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, related_name='webhooks')
    evento = models.CharField(max_length=50)
    payload = models.JSONField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.evento} - {self.pago.referencia}"

