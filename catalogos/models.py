from django.db import models


class CategoriasProductos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=140)
    portada = models.ImageField(upload_to="static/img/catalogos/categoria-productos/")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
