from django.contrib import admin
from django.urls import path, include
from usuarios import views


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        include('usuarios.urls')
    ),

    path(
        'productos/',
        include('productos.urls')
    ),

    path(
        'proveedores/',
        include('proveedores.urls')
    ),
    path(
        'inventario/',
        include('inventario.urls')
    ),
    path(
        '',
        views.inicio,
        name='inicio'
    ),
]