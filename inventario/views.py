from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import MovimientoForm
from .models import MovimientoInventario
from alertas.models import Alerta

@login_required
def registrar_movimiento(request):

    if request.method == 'POST':

        form = MovimientoForm(request.POST)

        if form.is_valid():

            movimiento = form.save(
                commit=False
            )

            producto = movimiento.producto

            if movimiento.tipo == 'ENTRADA':

                producto.stock += movimiento.cantidad

            else:

                if movimiento.cantidad > producto.stock:

                    messages.error(
                        request,
                        'Stock insuficiente para realizar la salida.'
                    )

                    return render(
                        request,
                        'inventario/formulario.html',
                        {'form': form}
                    )

                producto.stock -= movimiento.cantidad

            movimiento.usuario = request.user

            producto.save()

            ###

            if producto.stock <= producto.stockMinimo:

                Alerta.objects.create(
                    producto=producto,
                    mensaje=(
                        f'El producto {producto.nombre} '
                        f'alcanzo el stock mínimo.'
                    )
        )

            ###

            movimiento.save()

            messages.success(
                request,
                'Movimiento registrado correctamente.'
            )

            return redirect('dashboard')

    else:

        form = MovimientoForm()

    return render(
        request,
        'inventario/formulario.html',
        {'form': form}
    )