from django.db import models


class Alerta(models.Model):

    ESTADOS = [
        ('ACTIVA', 'Activa'),
        ('ATENDIDA', 'Atendida'),
    ]

    idAlerta = models.AutoField(
        primary_key=True
    )

    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.CASCADE
    )

    mensaje = models.CharField(
        max_length=255
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='ACTIVA'
    )

    def __str__(self):
        return self.mensaje