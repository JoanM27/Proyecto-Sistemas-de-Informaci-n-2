from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Proveedor
from .forms import ProveedorForm


@login_required
def lista_proveedores(request):

    proveedores = Proveedor.objects.all()

    return render(
        request,
        'proveedores/lista.html',
        {'proveedores': proveedores}
    )


@login_required
def crear_proveedor(request):

    if request.method == 'POST':

        form = ProveedorForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Proveedor registrado correctamente.'
            )

            return redirect('lista_proveedores')

    else:

        form = ProveedorForm()

    return render(
        request,
        'proveedores/formulario.html',
        {
            'form': form,
            'titulo': 'Nuevo Proveedor'
        }
    )


@login_required
def editar_proveedor(request, id):

    proveedor = get_object_or_404(
        Proveedor,
        idProveedor=id
    )

    if request.method == 'POST':

        form = ProveedorForm(
            request.POST,
            instance=proveedor
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Proveedor actualizado correctamente.'
            )

            return redirect('lista_proveedores')

    else:

        form = ProveedorForm(
            instance=proveedor
        )

    return render(
        request,
        'proveedores/formulario.html',
        {
            'form': form,
            'titulo': 'Editar Proveedor'
        }
    )


@login_required
def eliminar_proveedor(request, id):

    proveedor = get_object_or_404(
        Proveedor,
        idProveedor=id
    )

    if request.method == 'POST':

        proveedor.delete()

        messages.success(
            request,
            'Proveedor eliminado correctamente.'
        )

        return redirect('lista_proveedores')

    return render(
        request,
        'proveedores/eliminar.html',
        {'proveedor': proveedor}
    )