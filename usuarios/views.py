from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from productos.models import Producto
from alertas.models import Alerta
from django.db import models
from django.shortcuts import redirect
def registro(request):

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        confirmar = request.POST.get('confirmar')

        if password != confirmar:
            messages.error(
                request,
                'Las contraseñas no coinciden.'
            )
            return redirect('registro')

        if User.objects.filter(username=usuario).exists():
            messages.error(
                request,
                'El nombre de usuario ya existe.'
            )
            return redirect('registro')

        user = User.objects.create_user(
            username=usuario,
            email=correo,
            password=password
        )

        user.first_name = nombre
        user.save()

        messages.success(
            request,
            'Usuario registrado correctamente.'
        )

        return redirect('login')

    return render(
        request,
        'usuarios/registro.html'
    )


def iniciar_sesion(request):

    if request.method == 'POST':

        usuario = request.POST.get('usuario')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=usuario,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        messages.error(
            request,
            'Usuario o contraseña incorrectos.'
        )

    return render(
        request,
        'usuarios/login.html'
    )


def cerrar_sesion(request):

    logout(request)

    return redirect('login')


@login_required
def dashboard(request):

    productos = Producto.objects.all()

    total_productos = sum(
        producto.stock
        for producto in productos
    )

    valor_inventario = sum(
        producto.stock * producto.precio
        for producto in productos
    )

    productos_criticos = productos.filter(
        stock__lte=models.F('stockMinimo')
    )

    total_alertas = Alerta.objects.filter(
        estado='ACTIVA'
    ).count()

    return render(
        request,
        'usuarios/dashboard.html',
        {
            'total_productos': total_productos,
            'valor_inventario': valor_inventario,
            'total_alertas': total_alertas,
            'productos_criticos': productos_criticos,
        }
    )
def inicio(request):
    return redirect('login')