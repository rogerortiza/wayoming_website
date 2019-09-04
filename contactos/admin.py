""" Information to see in the admin Panel """
from django import forms
from django.contrib import admin
from .models import Clientes, Proveedores

# Register your models here.
@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    """ Information to display """
    list_display = ('nombre_completo', 'telefono', 'email', 'fecha_registro')
    fields = ('nombre', 'apellidos', 'direccion', 'colonia', 'ciudad', 'estado', 'pais', 'cp', 'telefono', 'email')


@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    """ Information to display """
    list_display = ('nombre', 'razon_social', 'telefono', 'email', 'fecha_registro')
    fields = ('nombre', 'razon_social', 'rfc', 'direccion', 'colonia', 'ciudad', 'estado', 'pais', 'cp', 'telefono', 'email')
