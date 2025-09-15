from carrito.models import Carrito, LineaCarrito, Cupon
from productos.models import Producto, Categoria
from django.contrib.auth.models import User
from pagos.models import Pago


def run():
  print("Borrando la base de datos...\n")
  Categoria.objects.all().delete()
  print("Categorias borradas")
  Producto.objects.all().delete()
  print("Productos borrados")
  Carrito.objects.all().delete()
  print("Carritos borrados")
  LineaCarrito.objects.all().delete()
  print("Lineas de carrito borradas")
  Cupon.objects.all().delete()
  print("Cupones borrados")
  Pago.objects.all().delete()
  print("Pagos borrados")
