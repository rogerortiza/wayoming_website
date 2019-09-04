from django.shortcuts import render
from django.views.generic import ListView
from .models import Clientes


class ClientesList(ListView):
    model = Clientes
    template_name = "contactos/lista_clientes.html"
    context_object_name = "clientes_list"
