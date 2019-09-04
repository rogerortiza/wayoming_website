""" Models for Inventario App"""
# noinspection PyUnresolvedReferences
from django.urls import reverse
# noinspection PyUnresolvedReferences
from django.db import models
# noinspection PyUnresolvedReferences
from catalogos.models import CategoriasProductos


class RegistroFecha(models.Model):
    """ This Model is about registration of products, stores and so on. """

    class Meta:
        """ Converting this class to abstract """
        abstract = True

    fecha_registro = models.DateTimeField(blank=True, auto_now_add=True)
    fecha_actulizado = models.DateTimeField(blank=True, auto_now=True)


class Productos(RegistroFecha):
    """ This Model is in order to register all the products """

    class Meta:
        """ New class name for admin panel """
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    GENERO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('N', 'Niño'),
        ('U', 'Unisex')
    )

    id = models.AutoField(primary_key=True)
    no_control = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriasProductos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(blank=True, null=True, max_length=500)
    estilo = models.CharField(blank=True, null=True, max_length=140)
    costo = models.DecimalField(max_digits=7, decimal_places=2)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    almacen = models.CharField(blank=True, null=True, max_length=100, default="Centro")
    foto = models.ImageField(upload_to="static/img/productos/")
    publico = models.CharField(blank=True, max_length=100, choices=GENERO)

    def cantidad(self):
        """ Este metodo regresa la cantidad que existe de cada producto """
        return sum(self.detalleproducto_set.all().values_list('cantidad', flat=True))

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """
        Este metodo regresa la url absoluta de un producto para poder redireccionar al
        usuario al detalle del producto
        """
        return reverse('detalle-producto', args=[str(self.id)])

    def save(self, *args, **kwargs): # pylint: disable=W0221
        if not self.no_control:
            last = Productos.objects.latest('id')
            last_no_control = int(last.no_control[5:]) + 1
            self.no_control = "WAY00" + str(last_no_control)

        super(Productos, self).save(*args, **kwargs)
