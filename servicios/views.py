from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Producto, Categoria, Color, City, Province, District
from .serializer import ProductosSerializer, CategoriasSerializer, ColorSerializer, UserSerializer, RegisterSerializer, CitySerializer, ProvinceSerializer, DistrictSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
# para registar un numero usuario
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework
from knox.models import AuthToken

# knox
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView


class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer
    filter_backends = [DjangoFilterBackend]


class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasSerializer
    filter_backends = [DjangoFilterBackend]

class ColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [DjangoFilterBackend]

class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ProvinceView(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class DistrictView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class ProductByCategoryList(generics.ListAPIView):

    serializer_class = ProductosSerializer

    def get_queryset(self):
        idcategoria = self.kwargs['id']
        return Producto.objects.filter(idcategoria=idcategoria)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
