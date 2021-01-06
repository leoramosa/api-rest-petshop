from django.contrib import admin
from .models import Carritocompras, Cliente, Color, Comentario, Foto, Genero, Marca, Modelo, Pago, Talla
from .models import Historialconsulta, Tipopago, Tipoproducto, Usuario, Valoracion, Venta, VentaProducto
from .models import Producto, Categoria, City, Province, District, Imagencolor, Portada

""" admin.site.register(Carritocompras) """
""" admin.site.register(Cliente) """
admin.site.register(Color)
admin.site.register(Talla)
""" admin.site.register(Comentario) """
""" admin.site.register(Foto) """
""" admin.site.register(Genero) """
""" admin.site.register(Marca) """
""" admin.site.register(Modelo) """
""" admin.site.register(Pago) """
admin.site.register(Producto)
""" admin.site.register(Historialconsulta) """
""" admin.site.register(Tipopago) """
""" admin.site.register(Tipoproducto) """
admin.site.register(Usuario)
""" admin.site.register(Valoracion) """
""" admin.site.register(Venta) """
""" admin.site.register(VentaProducto) """
admin.site.register(Categoria)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Imagencolor)
admin.site.register(Portada)


# Register your models here.
