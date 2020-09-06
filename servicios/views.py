from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Producto, Categoria, Color
from .serializer import ProductosSerializer, CategoriasSerializer, ColorSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import filters
# para registar un numero usuario


class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductosSerializer
    filter_backends = [DjangoFilterBackend]


class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasSerializer


class ColorView(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
