from django.utils import timezone
from carrito.models import Carrito, LineaCarrito, Cupon
from productos.models import Producto, Categoria, Favorito
from django.contrib.auth.models import User
from pagos.models import Pago
from pprint import pprint



def run():
  print("Hello world!")
  print("Probando la base de datos...\n")
  Favoritos = Favorito.objects.all()
  print("Favoritos encontrados:")
  pprint(Favoritos)