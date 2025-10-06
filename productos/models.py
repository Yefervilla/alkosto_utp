from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    parend_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategorias')
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    valor = models.FloatField()

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(valor__gte=0.0, valor__lte=5.0), name='valor_rango_0_5'),
        ]
        unique_together = ('user', 'producto') 

    def __str__(self):
        return f"{self.user.username} → {self.producto.nombre}: {self.valor}"