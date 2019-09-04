""" Models for Productos App"""
from django.db import models
from inventario.models import Productos


class BaseProductos(models.Model):
    """ This Model store the base fields for all products models """
    class Meta:
        """ Abstact Class """
        abstract = True

    COLORES = (
        ('black', 'Negro'),
        ('brown', 'Cafe'),
        ('yellow', 'Miel'),
        ('blue', 'Azul'),
        ('grey', 'Gris'),
        ('Red', 'Rojo'),
    )

    color = models.CharField(blank=True, max_length=100, choices=COLORES)
    size = models.CharField(blank=True, max_length=100)
    cantidad = models.IntegerField(blank=True, null=True)


class DetalleProducto(BaseProductos):
    """ This Model store info about all Botas """
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto.nombre
