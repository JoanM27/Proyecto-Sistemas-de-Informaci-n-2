from django.db import models


class Proveedor(models.Model):

    idProveedor = models.AutoField(
        primary_key=True
    )

    nombre = models.CharField(
        max_length=100
    )

    telefono = models.CharField(
        max_length=20
    )

    correo = models.EmailField()

    direccion = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.nombre