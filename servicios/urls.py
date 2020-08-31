from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', views.ProductoView,)
router.register('categorias', views.CategoriaView,)
router.register('color', views.ColorView,)

urlpatterns = [
    path('', include(router.urls))
]
