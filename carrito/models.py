from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

class Cupon(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    descuento = models.DecimalField(max_digits=2, decimal_places=2)  # porcentaje
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo

class Carrito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    cupon = models.ForeignKey(Cupon, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total(self):
        total = sum([linea.subtotal() for linea in self.lineas.all()])
        if self.cupon and self.cupon.activo:
            total *= (1 - self.cupon.descuento / 100)
        return total

    def __str__(self):
        if self.user:
            return f"Carrito de {self.user.username}"
        return f"Carrito anónimo #{self.id}"
    

class LineaCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name="lineas", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    