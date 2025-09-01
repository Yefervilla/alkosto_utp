from django.shortcuts import render, redirect
from .models import Producto 

# Lista de productos

def lista_productos(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    if categoria_id:
        productos = Producto.objects.filter(categoria_id=categoria_id)
    else:
        productos = Producto.objects.all()
    return render(request, "productos/productos.html", {"productos": productos, "categorias": categorias, "categoria_id": categoria_id})

# Crear producto

from .models import Producto, Categoria
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'categoria']

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, "productos/crear_producto.html", {"form": form})