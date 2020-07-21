from django.db import models
from autoslug import AutoSlugField

class Carritocompras(models.Model):
    idcarrito = models.IntegerField(db_column='idCarrito', primary_key=True)  # Field name made lowercase.
    fechacarrito = models.DateTimeField(db_column='fechaCarrito', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    preciototal = models.FloatField(db_column='precioTotal', blank=True, null=True)  # Field name made lowercase.
    FK_DetalleCarrito = models.ManyToManyField('Producto')
    class Meta:
        managed = True
        db_table = 'carritocompras'


class Cliente(models.Model):

    nomcliente = models.CharField(db_column='nomCliente', max_length=200)  # Field name made lowercase.
    direccliente = models.CharField(db_column='direcCliente', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ruc = models.CharField(db_column='RUC', max_length=11, blank=True, null=True)  # Field name made lowercase.
    fechanac = models.DateField(db_column='fechaNac', blank=True, null=True)  # Field name made lowercase.
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    telefono3 = models.CharField(max_length=20, blank=True, null=True)
    idusuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='idUsuario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'cliente'
    
    def __str__(self):
        return self.nomcliente




class Talla(models.Model):

    nomtalla = models.CharField(db_column='nomTalla', max_length=60, blank=True, null=True)
    numtalla = models.IntegerField(db_column='NumTalla', blank=True, null=True)  # Field name made lowercase.
    value= models.CharField(db_column='numvalue', max_length=60, blank=True, null=True)  # Field name made lowercase.
    #productotalla= models.ForeignKey(Producto, related_name='tallas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomtalla

class Comentario(models.Model):
    idcomentario = models.IntegerField(db_column='idComentario', primary_key=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=200)  # Field name made lowercase.
    idprod = models.ForeignKey('Producto', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'comentario'


class Foto(models.Model):
    imgfoto = models.ImageField(upload_to="productos",blank=True)  # Field name made lowercase.

    idprod = models.ForeignKey('Producto', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'foto'


class Genero(models.Model):

    nomgenero = models.CharField(db_column='nomGenero', max_length=60)  # Field name made lowercase.
    #productogenero = models.ForeignKey(Producto, related_name='generos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomgenero


class Historialconsulta(models.Model):
    idconsulta = models.IntegerField(db_column='idConsulta', primary_key=True)  # Field name made lowercase.
    fechaconsulta = models.DateField(db_column='fechaConsulta', blank=True, null=True)  # Field name made lowercase.
    horaconsulta = models.DateTimeField(db_column='HoraConsulta', blank=True, null=True)  # Field name made lowercase.
    nivelnavegacion = models.CharField(db_column='NivelNavegacion', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idprod = models.ForeignKey('Producto', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'historialconsulta'



class Marca(models.Model):
  
    nommarca = models.CharField(db_column='nomMarca', max_length=60)  # Field name made lowercase.
    #productomarca = models.ForeignKey(Producto, related_name='marcas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nommarca


class Modelo(models.Model):

    nommodelo = models.CharField(db_column='nomModelo', max_length=60,  blank=True, null=True)  # Field name made lowercase.
    descmodelo = models.CharField(db_column='descModelo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    #productomodelo = models.ForeignKey(Producto, related_name='tipomodelo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nommodelo


class Pago(models.Model):
    idpago = models.IntegerField(db_column='idPago', primary_key=True)  # Field name made lowercase.
    fechapago = models.DateTimeField(db_column='fechaPago')  # Field name made lowercase.
    importepago = models.FloatField(db_column='importePago')  # Field name made lowercase.
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)
    idtipopago = models.ForeignKey('Tipopago', on_delete=models.CASCADE, db_column='idTipoPago', blank=True, null=True)  # Field name made lowercase.
    idventa = models.ForeignKey('Venta', on_delete=models.CASCADE, db_column='idVenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pago'

class Categoria(models.Model):
    #idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(max_length=200, blank=True, null=True)
    fotocategoria = models.ImageField(upload_to="productos",blank=True)  # Field name made lowercase.
    imagen = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.
    activo = models.IntegerField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombrecategoria

    class Meta:
        managed = True
        db_table = 'categoria'

class Usuario(models.Model):
    
    nomusuario = models.CharField(db_column='nomUsuario', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipousuario = models.CharField(db_column='tipousuario', max_length=200, blank=True, null=True)  # Field name made lowercase.
    apeusuario = models.CharField(db_column='apeUsuario', max_length=200, blank=True, null=True)  # Field name made lowercase.
    correousuario = models.CharField(db_column='correoUsuario', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechainscripcion = models.DateTimeField(db_column='fechaInscripcion', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(blank=True, null=True)
    #productousuario = models.ForeignKey(Producto, related_name='usuarios', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomusuario

    class Meta:
        managed = True
        db_table = 'usuario'

class Tipoproducto(models.Model):
    #idtipoproducto = models.IntegerField(db_column='idTipoProducto', primary_key=True)  # Field name made lowercase.
    nomtipoproducto = models.CharField(db_column='nomTipoProducto', max_length=60)  # Field name made lowercase.
    #productotipo = models.ForeignKey(Producto, related_name='tipoproducto', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomtipoproducto

    class Meta:
        managed = True
        db_table = 'tipoproducto'

class Color(models.Model):
    nomcolor = models.CharField(db_column='nomColor', max_length=60, blank=True, null=True)  # Field name made lowercase.
    numcolor = models.CharField(db_column='numColor', max_length=60, blank=True, null=True)  # Field name made lowercase.
    value= models.CharField(db_column='numvalue', max_length=60, blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return self.nomcolor



class Producto(models.Model):
    #idprod = models.AutoField(db_column='idprod', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=200, blank=True, null=True)
    fotoportada = models.ImageField(upload_to="productos",blank=True)  # Field name made lowercase.
    imagen = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.
    #cantidad_stock = models.CharField(db_column='Cantidad_Stock', max_length=18, blank=True, null=True)  # Field name made lowercase.
    cantidadstock = models.CharField(db_column='CantidadStock', max_length=18, blank=True, null=True)  # Field name made lowercase.
    precioreal = models.IntegerField(db_column='PrecioReal', blank=True, null=True)  # Field name made lowercase.
    preciopromocion = models.IntegerField(db_column='PrecioPromocion', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    brevedescripcion = models.CharField(db_column='breveDescripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prodoferta = models.IntegerField(db_column='ProdOferta', blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.CharField(db_column='FechaCreacion', max_length=18, blank=True, null=True)  # Field name made lowercase.
    idmodelo = models.ForeignKey(Modelo, on_delete=models.CASCADE,)  # Field name made lowercase.
      # Field name made lowercase.
    idcolor = models.ManyToManyField(Color,)
    idtallaproducto = models.ManyToManyField(Talla,)
    idgenero = models.ForeignKey(Genero, on_delete=models.CASCADE,)  # Field name made lowercase.
    idmarca = models.ForeignKey(Marca, on_delete=models.CASCADE, )  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, )  # Field name made lowercase.
    idtipoproducto = models.ForeignKey(Tipoproducto, on_delete=models.CASCADE)  # Field name made lowercase.
    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Field name made lowercase.
    slug = AutoSlugField(populate_from='nombre')
    mostrarpaginicio = models.IntegerField(db_column='mostrarPagInicio')  # Field name made lowercase.
    activo = models.IntegerField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'producto'

    def __str__(self):
        return self.nombre

        


class Tipopago(models.Model):
    idtipopago = models.IntegerField(db_column='idTipoPago', primary_key=True)  # Field name made lowercase.
    nomtipopago = models.CharField(db_column='nomTipoPago', max_length=50)  # Field name made lowercase.

    def __str__(self):
        return self.nomtipopago

    class Meta:
        managed = True
        db_table = 'tipopago'



class Valoracion(models.Model):
    idvaloracion = models.IntegerField(db_column='id_Valoracion', primary_key=True)  # Field name made lowercase.
    puntage = models.IntegerField(db_column='Puntage', blank=True, null=True)  # Field name made lowercase.
    idprod = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'valoracion'


class Venta(models.Model):
    idventa = models.IntegerField(db_column='idVenta', primary_key=True)  # Field name made lowercase.
    fechaventa = models.DateTimeField(db_column='fechaVenta')  # Field name made lowercase.
    importeventa = models.FloatField(db_column='importeVenta')  # Field name made lowercase.
    fechaentrega = models.DateTimeField(db_column='fechaEntrega', blank=True, null=True)  # Field name made lowercase.
    direccionentrega = models.CharField(db_column='direccionEntrega', max_length=200, blank=True, null=True)  # Field name made lowercase.
    observacionentrega = models.CharField(db_column='observacionEntrega', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estadoentrega = models.IntegerField(db_column='estadoEntrega', blank=True, null=True)  # Field name made lowercase.
    observacionestadoentrega = models.CharField(db_column='observacionEstadoEntrega', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='idCliente', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'venta'


class VentaProducto(models.Model):
    iddetalle = models.IntegerField(db_column='idDetalle', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField()
    precio = models.IntegerField(db_column='Precio')  # Field name made lowercase.
    subtotal = models.IntegerField()
    descuento = models.IntegerField(blank=True, null=True)
    idprod = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Field name made lowercase.
    idventa = models.ForeignKey(Venta, on_delete=models.CASCADE, db_column='idVenta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'venta_producto'
