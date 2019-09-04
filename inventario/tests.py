""" Unittest para el modulo de inventario """
from django.test import TestCase
from catalogos.models import CategoriasProductos
from inventario.models import Productos


class TestInventario(TestCase):
    """ Clase para crear test de Inventario """

    def setUp(self):
        """
        Configuracion inicial para realizar la prueba.
        Se crea una categoria.
        Se crea un producto y se le asgina a una categoria
        :return:
        """
        categoria = CategoriasProductos.objects.create()
        Productos.objects.create(
            no_control='999999', categoria=categoria, nombre='Piteado_test',
            descripcion='cinto_test', almacen='Centro_test', costo=300,
            precio=700.00
        )
        self.producto = Productos.objects.get(nombre="Piteado_test")

    def test_producto(self):
        """
        El producto debe ser una instancia de Productos
        Se obtiene de el producto q se creo al inicio de la prueba y se
        vetifica q el producto sea de Productos
        :return: boolean
        """
        self.assertEqual(True, isinstance(self.producto, Productos))

    def test_producto_update(self):
        """
        El producto puede ser actualizado
        :return: boolean
        """
        self.producto.costo = 500
        self.producto.save()
        self.assertEqual(500, self.producto.costo)
