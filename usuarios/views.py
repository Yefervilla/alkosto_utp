from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from productos.models import Producto
from django.contrib.auth.models import User
from django.contrib import messages

# pagina de inicio

def home(request):
    return render(request, "usuarios/home.html")

# login

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else :
            return HttpResponse("usuario o contraseña incorrecta")
        
    return render(request, "usuarios/login.html")


#logout

def user_logout(request):
    logout (request)
    return redirect("login")


def user_register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            return HttpResponse("Las contraseñas no coinciden")
        if User.objects.filter(username=username).exists():
            return HttpResponse("El usuario ya existe")
        
        # Crear usuario
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("login")
    
    return render(request, "usuarios/register.html")
