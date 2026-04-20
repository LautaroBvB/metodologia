from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Producto, DatosUsuario


def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user:
            user = authenticate(request, username=user.username, password=password)

        if user:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def register_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        mail = request.POST.get('mail')
        telefono = request.POST.get('telefono')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'las contraseñas no coinciden'})

        user = User.objects.create_user(
            username=mail,
            email=mail,
            password=password,
            first_name=nombre,
            last_name=apellido
        )

        DatosUsuario.objects.create(
            user=user,
            telefono=telefono
        )

        return redirect('login')

    return render(request, 'register.html')