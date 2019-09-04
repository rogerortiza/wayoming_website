from django.contrib import admin
from .models import CategoriasProductos

@admin.register(CategoriasProductos)
class CategoriasProductos(admin.ModelAdmin):
    list_display = ('id', 'nombre')
