from django.contrib import admin
from django.utils.html import format_html
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


class ImagencolorAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="150" height="150" />'.format(obj.imagen.url))
    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag', 'state']


admin.site.register(Imagencolor, ImagencolorAdmin)

admin.site.register(Portada)


# Register your models here.
