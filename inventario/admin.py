""" Admin panel models register """
from django.contrib import admin
from productos.models import DetalleProducto
from .models import Productos


class DetalleProductoInline(admin.TabularInline):
    """
    Esta clase se usa como Inline para los detalles del producto.
    """
    model = DetalleProducto
    can_delete = False

class ProductosAdmin(admin.ModelAdmin):
    """ Product information """
    list_display = ('id', 'no_control', 'nombre', 'descripcion', 'cantidad', 'fecha_registro')
    exclude = ('no_control',)
    inlines = [DetalleProductoInline,]

admin.site.register(Productos, ProductosAdmin)
