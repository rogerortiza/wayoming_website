""" Models related with contacts of Wayomig """
from django.db import models
from inventario.models import RegistroFecha

# Create your models here.
class BaseContacts(models.Model):
    """ Modelo to store directions of Contacts """
    class Meta:
        """ Converting to Abstract Model """
        abstract = True

    direccion = models.CharField(max_length=100)
    colonia = models.CharField(blank=True, max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, default='Durango')
    pais = models.CharField(max_length=100, default='Mexico')
    cp = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(blank=True, max_length=100)

class Clientes(BaseContacts, RegistroFecha):
    """ Clientes info """
    class Meta:
        """ Extra info """
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    def nombre_completo(self):
        """ Method to return the fullname of a client """
        return self.nombre+" "+self.apellidos

    def __str__(self):
        return self.nombre+" "+self.apellidos

class Proveedores(BaseContacts, RegistroFecha):
    """ Proveedores info """
    class Meta:
        """ Extra info """
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(blank=True, max_length=100)
    rfc = models.CharField(blank=True, max_length=100)
