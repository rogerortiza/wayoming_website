from rest_framework import routers
from inventario.viewsets import ProductosViewset

router = routers.DefaultRouter()
router.register(r'productos', ProductosViewset)
