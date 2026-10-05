from django.db import models
from django.contrib.auth.models import User


class MovimientoInventario(models.Model):

    TIPOS = [
        ('ENTRADA', 'Entrada (+)'),
        ('SALIDA', 'Salida (-)'),
    ]

    idMovimiento = models.AutoField(
        primary_key=True
    )

    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.CASCADE
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPOS
    )

    cantidad = models.PositiveIntegerField()

    justificacion = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return f'{self.tipo} - {self.producto}'