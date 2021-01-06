from rest_framework import serializers
from .models import Producto, Categoria, Color, City, Province, District, Portada
from django.contrib.auth.models import User
# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"
        depth = 2


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class PortadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portada
        fields = "__all__"
        depth = 1


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
        depth = 1
