from django.utils import timezone
from carrito.models import Carrito, LineaCarrito, Cupon
from productos.models import Producto, Categoria
from django.contrib.auth.models import User
from pagos.models import Pago
from pprint import pprint

def delete():
  print("Borrando la base de datos...\n")
  Categoria.objects.all().delete()
  Producto.objects.all().delete()
  Carrito.objects.all().delete()
  LineaCarrito.objects.all().delete()
  Cupon.objects.all().delete()
  Pago.objects.all().delete()

def crearCategorias():
  print("Llenando la base de datos...\n")
  # Crear categorías
  Categoria.objects.get_or_create(
    nombre="Computadores Portatiles"
  )
  Categoria.objects.get_or_create(
      nombre="Portatiles gaming", parend_id=Categoria.objects.get(nombre="Computadores Portatiles")
  )
  Categoria.objects.get_or_create(
      nombre="Computadores Empresariales", parend_id=Categoria.objects.get(nombre="Computadores Portatiles")
  )
  
  Categorias = Categoria.objects.all()
  print("Categorias creadas:")
  pprint(Categorias)

def createProductos():
  Producto.objects.get_or_create(
    nombre="Computador Portátil Gamer ASUS TUF F 16\" Pulgadas FX607VJ",
    descripcion="Portátil ASUS ROG Strix G15 con procesador AMD Ryzen 7",
    precio=4500000,
    stock=10,
    categoria=Categoria.objects.get(nombre="Portatiles gaming")
  )

  Producto.objects.get_or_create(
    nombre="Computador Portátil HP 240 G8 14\" Pulgadas",
    descripcion="Portátil HP 240 G8 con procesador Intel Core i5",
    precio=2500000,
    stock=15,
    categoria=Categoria.objects.get(nombre="Computadores Empresariales")
  )

  Producto.objects.get_or_create(
    nombre="Computador Portátil Lenovo Ideapad 3 15ITL6",
    descripcion="Portátil Lenovo Ideapad 3 con procesador Intel Core i7",
    precio=3200000,
    stock=8,
    categoria=Categoria.objects.get(nombre="Computadores Empresariales")
  )

  Productos = Producto.objects.all()

  print("Productos creados:")
  pprint(Productos)



def run():
  delete()
  crearCategorias()
  createProductos()