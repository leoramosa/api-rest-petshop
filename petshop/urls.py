from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# para que carguen las iamgenes se tiene que incluir esto dos
from petshop import settings
from django.conf.urls.static import static
from servicios import views

# knox
from knox import views as knox_views


urlpatterns = [
    path('admin/', admin.site.urls),
    url('servicios/', include('servicios.urls')),
    path('servicios/categorias_name/<int:id>',
         views.ProductByCategoryList.as_view()),

    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
