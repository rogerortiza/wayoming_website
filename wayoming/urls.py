"""
wayoming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .routers import router
from django.contrib import admin
from django.urls import path, include
from dashboard.views import home
from contactos.views import ClientesList
from inventario.views import ProductosList, ProductoDetalle
from django.views.generic import TemplateView

#Setting custome titles
admin.site.site_header = "Wayoming Boot Shop"
admin.site.site_title = "Wayoming Boot Shop"
admin.site.index_title = "Wayoming Boot Shop"


urlpatterns = [
    path('', home, name="home"),
    path('dashboard/', TemplateView.as_view(template_name='dashboard/index.html')),
    path('lista-clientes/', ClientesList.as_view()),
    path('lista-productos/', TemplateView.as_view(template_name='inventario/lista_productos.html'), name='lista-productos'),
    path('detalle-producto/<pk>', ProductoDetalle.as_view(), name='detalle-producto'),
    path('wbs-admin/', admin.site.urls),
    path('search/', include('haystack.urls')),
    path('api/', include(router.urls)),
]
