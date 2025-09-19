from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User

# Create your models here.
class Favorito(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'producto')  
        
    def __str__(self):
        return f"{self.user.username} - {self.producto.nombre}"