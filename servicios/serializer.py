from rest_framework import serializers
from .models import Producto, Categoria, Color

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields="__all__"

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields="__all__"

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Color
        fields="__all__"

