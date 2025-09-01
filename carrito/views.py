from django.shortcuts import render, redirect, get_object_or_404
from productos.models import Producto
from .models import Carrito, LineaCarrito
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Cupon

def obtener_carrito(request):
    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(user=request.user)
    else:
        carrito_id = request.session.get("carrito_id")
        carrito = None
        if carrito_id:
            carrito = Carrito.objects.filter(id=carrito_id).first()
        if not carrito:
            carrito = Carrito.objects.create()
            request.session["carrito_id"] = carrito.id
    return carrito

def agregar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = obtener_carrito(request)
    linea, created = LineaCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        linea.cantidad += 1
        linea.save()
    return redirect("carrito_lista")  # nombre del URL

def carrito_lista(request):
    carrito = obtener_carrito(request)
    return render(request, "carrito/lista_carrito.html", {"carrito": carrito})

def eliminar_linea(request, linea_id):
    linea = get_object_or_404(LineaCarrito, id=linea_id)
    linea.delete()
    return redirect("carrito_lista")

@require_POST
def aplicar_cupon(request):
    carrito = obtener_carrito(request)
    codigo = request.POST.get("codigo")
    cupon = Cupon.objects.filter(codigo=codigo, activo=True).first()
    if cupon:
        carrito.cupon = cupon
        carrito.save()
    return redirect("carrito_lista")
