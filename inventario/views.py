""" Views para el modulo de Inventario """
from django.views.generic import DetailView, ListView
from .models import Productos


class ProductosList(ListView): # pylint: disable=too-many-ancestors
    """ Vista que regresa una lista de productos """
    model = Productos
    template_name = "inventario/lista_productos.html"
    context_object_name = "lista_productos"

class ProductoDetalle(DetailView): # pylint: disable=too-many-ancestors
    """ Vista que regresa el detalle de un Producto """
    model = Productos
    template_name = "productos/detalle_producto.html"
    queryset = Productos.objects.all()
    context_object_name = "producto"
