""" Serializers para los viewsets del Inventario API """
from rest_framework import serializers
from catalogos.models import CategoriasProductos
from .models import Productos


class CategoriaSerializer(serializers.ModelSerializer):
    """ Serializer para el modelo de Categorias """
    class Meta:
        """ Solo se serializan algunos campos """
        model = CategoriasProductos
        fields = ('id', 'portada', 'nombre')


class ProductosSerializer(serializers.ModelSerializer):
    """ Serializer para el modelo de Productos """
    categoria = CategoriaSerializer()
    foto = serializers.CharField(source='foto.url')
    colores = serializers.SerializerMethodField()
    numeros = serializers.SerializerMethodField()

    class Meta:
        """ Se asigna el model Productos y se serializan algunos campos """
        model = Productos
        fields = ('id', 'categoria', 'descripcion', 'estilo', 'foto', 'no_control', 'nombre',
                  'precio', 'publico', 'colores', 'numeros',)

    @staticmethod
    def get_colores(obj) -> list:
        """
        Este metodo se usa para regresar una lista con los colores disponibles
        para el producto
        :param obj:
        :return: ['red', 'black', 'etc']
        """
        colores = list(obj.detalleproducto_set.all().values_list('color', flat=True).distinct())
        return colores

    @staticmethod
    def get_numeros(obj) -> list:
        """
        Este metodo regresa un lista de numeros disponibles para el producto
        :param obj:
        :return: [6,7,8]
        """
        numeros = list(obj.detalleproducto_set.all().values_list('size', flat=True).distinct())
        return numeros
