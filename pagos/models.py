from django.db import models

class Pago(models.Model):
    METODOS = [
        ('MP', 'Mercado Pago'),
        ('PU', 'PayU Latam'),
        ('ST', 'Stripe'),
    ]
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]
    
    metodo = models.CharField(max_length=2, choices=METODOS)
    referencia = models.CharField(max_length=50, unique=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, choices=ESTADOS)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.referencia

class Webhook(models.Model):
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE, related_name='webhooks')
    evento = models.CharField(max_length=50)
    payload = models.JSONField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.evento} - {self.pago.referencia}"

