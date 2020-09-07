from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Producto, Categoria, Color
from .serializer import ProductosSerializer, CategoriasSerializer, ColorSerializer
from rest_framework import viewsets
from rest_framework import generics
# para registar un numero usuario


class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer


class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasSerializer


class ColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ProductByCategoryList(generics.ListAPIView):

    serializer_class = ProductosSerializer

    def get_queryset(self):
        idcategoria = self.kwargs['id']
        return Producto.objects.filter(idcategoria=idcategoria)
