""" Viwsets para el Inventario API """
from rest_framework import viewsets
from django_restql import DynamicFieldsMixin
from .models import Productos
from .serializers import ProductosSerializer


class ProductosViewset(DynamicFieldsMixin, viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """
    Este viewset regresa los productos que estan en el inventario.
    DynamicFieldsMixin: Se usa para poder implementar queries en las peticiones a la API
    (Graphql)
    """
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
