from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categorias', views.CategoriaView,)
router.register('city', views.CityView,)
router.register('province', views.ProvinceView,)
router.register('district', views.DistrictView,)
router.register('color', views.ColorView,)
router.register('productos', views.ProductoView,)


urlpatterns = [
    path('', include(router.urls)),
]
