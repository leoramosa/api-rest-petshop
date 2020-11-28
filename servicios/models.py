from django.db import models
from autoslug import AutoSlugField


class Carritocompras(models.Model):
    # Field name made lowercase.
    idcarrito = models.IntegerField(db_column='idCarrito', primary_key=True)
    # Field name made lowercase.
    fechacarrito = models.DateTimeField(
        db_column='fechaCarrito', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    preciototal = models.FloatField(
        db_column='precioTotal', blank=True, null=True)
    FK_DetalleCarrito = models.ManyToManyField('Producto')

    class Meta:
        managed = True
        db_table = 'carritocompras'


class Cliente(models.Model):

    # Field name made lowercase.
    nomcliente = models.CharField(db_column='nomCliente', max_length=200)
    # Field name made lowercase.
    direccliente = models.CharField(
        db_column='direcCliente', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    ruc = models.CharField(
        db_column='RUC', max_length=11, blank=True, null=True)
    # Field name made lowercase.
    fechanac = models.DateField(db_column='fechaNac', blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    telefono3 = models.CharField(max_length=20, blank=True, null=True)
    # Field name made lowercase.
    idusuario = models.ForeignKey(
        'Usuario', on_delete=models.CASCADE, db_column='idUsuario', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente'

    def __str__(self):
        return self.nomcliente


class Talla(models.Model):

    nomtalla = models.CharField(
        db_column='nomTalla', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    numtalla = models.IntegerField(db_column='NumTalla', blank=True, null=True)
    # Field name made lowercase.
    value = models.CharField(db_column='numvalue',
                             max_length=60, blank=True, null=True)
    # productotalla= models.ForeignKey(Producto, related_name='tallas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomtalla


class Comentario(models.Model):
    # Field name made lowercase.
    idcomentario = models.IntegerField(
        db_column='idComentario', primary_key=True)
    # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=200)
    # Field name made lowercase.
    idprod = models.ForeignKey('Producto', on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'comentario'


class Foto(models.Model):
    # Field name made lowercase.
    imgfoto = models.ImageField(upload_to="productos", blank=True)

    # Field name made lowercase.
    idprod = models.ForeignKey(
        'Producto', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'foto'


class Genero(models.Model):

    # Field name made lowercase.
    nomgenero = models.CharField(db_column='nomGenero', max_length=60)
    # productogenero = models.ForeignKey(Producto, related_name='generos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomgenero


class Historialconsulta(models.Model):
    # Field name made lowercase.
    idconsulta = models.IntegerField(db_column='idConsulta', primary_key=True)
    # Field name made lowercase.
    fechaconsulta = models.DateField(
        db_column='fechaConsulta', blank=True, null=True)
    # Field name made lowercase.
    horaconsulta = models.DateTimeField(
        db_column='HoraConsulta', blank=True, null=True)
    # Field name made lowercase.
    nivelnavegacion = models.CharField(
        db_column='NivelNavegacion', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    idprod = models.ForeignKey(
        'Producto', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'historialconsulta'


class Marca(models.Model):

    # Field name made lowercase.
    nommarca = models.CharField(db_column='nomMarca', max_length=60)
    # productomarca = models.ForeignKey(Producto, related_name='marcas', on_delete=models.CASCADE)

    def __str__(self):
        return self.nommarca


class Modelo(models.Model):

    # Field name made lowercase.
    nommodelo = models.CharField(
        db_column='nomModelo', max_length=60,  blank=True, null=True)
    descmodelo = models.CharField(
        db_column='descModelo', max_length=200, blank=True, null=True)
    
    # productomodelo = models.ForeignKey(Producto, related_name='tipomodelo', on_delete=models.CASCADE)

    def __str__(self):
        return self.nommodelo


class City(models.Model):

    name = models.CharField(max_length=60,  blank=True, null=True)
    delivery = models.BooleanField(default=True, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Province(models.Model):

    name = models.CharField(max_length=60,  blank=True, null=True)
    idcity = models.ForeignKey(City, on_delete=models.CASCADE, )
    delivery = models.BooleanField(default=True, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)
    tienda = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name


class District(models.Model):

    name = models.CharField(max_length=60,  blank=True, null=True)
    idprovince = models.ForeignKey(Province, on_delete=models.CASCADE, )
    delivery = models.BooleanField(default=True, blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)
    tienda = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name
    


class Pago(models.Model):
    # Field name made lowercase.
    idpago = models.IntegerField(db_column='idPago', primary_key=True)
    # Field name made lowercase.
    fechapago = models.DateTimeField(db_column='fechaPago')
    # Field name made lowercase.
    importepago = models.FloatField(db_column='importePago')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)
    # Field name made lowercase.
    idtipopago = models.ForeignKey(
        'Tipopago', on_delete=models.CASCADE, db_column='idTipoPago', blank=True, null=True)
    # Field name made lowercase.
    idventa = models.ForeignKey(
        'Venta', on_delete=models.CASCADE, db_column='idVenta', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pago'


class Categoria(models.Model):
    # idcategoria = models.AutoField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(max_length=200, blank=True, null=True)
    # Field name made lowercase.

    photo_category_product = models.ImageField(
        upload_to="productos", blank=True, null=True)
    fotocategoria = models.ImageField(
        upload_to="productos", blank=True, null=True)
    fotocategoria1 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    fotocategoria2 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    fotocategoria3 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    fotocategoria4 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    # Field name made lowercase.
    imagen = models.CharField(max_length=200, blank=True, null=True)
    activo = models.IntegerField()
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    iconcategory = models.ImageField(
        upload_to="productos", blank=True, null=True)

    def __str__(self):
        return self.nombrecategoria

    class Meta:
        managed = True
        db_table = 'categoria'


class Usuario(models.Model):

    # Field name made lowercase.
    nomusuario = models.CharField(
        db_column='nomUsuario', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    tipousuario = models.CharField(
        db_column='tipousuario', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    apeusuario = models.CharField(
        db_column='apeUsuario', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    correousuario = models.CharField(
        db_column='correoUsuario', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    fechainscripcion = models.DateTimeField(
        db_column='fechaInscripcion', blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    # productousuario = models.ForeignKey(Producto, related_name='usuarios', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomusuario

    class Meta:
        managed = True
        db_table = 'usuario'


class Tipoproducto(models.Model):
    # idtipoproducto = models.IntegerField(db_column='idTipoProducto', primary_key=True)  # Field name made lowercase.
    # Field name made lowercase.
    nomtipoproducto = models.CharField(
        db_column='nomTipoProducto', max_length=60)
    # productotipo = models.ForeignKey(Producto, related_name='tipoproducto', on_delete=models.CASCADE)

    def __str__(self):
        return self.nomtipoproducto

    class Meta:
        managed = True
        db_table = 'tipoproducto'


class Color(models.Model):
    # Field name made lowercase.
    nombrecolor = models.CharField(
        db_column='nombreColor', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    numbercolor = models.CharField(
        db_column='numberColor', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    valuecolor = models.CharField(
        db_column='valuColor', max_length=60, blank=True, null=True)
    imagencolor1 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    imagencolor2 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    imagencolor3 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    imagencolor4 = models.ImageField(
        upload_to="productos", blank=True, null=True)
    imagencolor5 = models.ImageField(
        upload_to="productos", blank=True, null=True)

    def __str__(self):
        return self.nombrecolor

    class Meta:
        managed = True
        db_table = 'nombrecolor'


class Producto(models.Model):
    # idprod = models.AutoField(db_column='idprod', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=200, blank=True, null=True)
    # Field name made lowercase.
    fotoportadaactivo = models.IntegerField(blank=True, null=True)
    fotoportada = models.ImageField(
        upload_to="productos", blank=True, null=True)
    fotoprincipal = models.ImageField(
        upload_to="productos", blank=True, null=True)
    # Field name made lowercase.
    # cantidad_stock = models.CharField(db_column='Cantidad_Stock', max_length=18, blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    cantidadstock = models.CharField(
        db_column='CantidadStock', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    precionormal = models.IntegerField(
        db_column='PrecioNormal', blank=True, null=True)
    # Field name made lowercase.
    preciointernet = models.IntegerField(
        db_column='PrecioInternet', blank=True, null=True)
    preciopromocion = models.IntegerField(
        db_column='PrecioPromocion', blank=True, null=True)
    # Field name made lowercase.
    preciooferta = models.IntegerField(
        db_column='ProdOferta', blank=True, null=True)
    # Field name made lowercase.
    descripcion = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    brevedescripcion = models.TextField(blank=True, null=True)
    # Field name made lowercase.
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    # Field name made lowercase.
    idmodelo = models.ForeignKey(Modelo, on_delete=models.CASCADE,)
    # Field name made lowercase.
    idcolor = models.ManyToManyField(Color,)
    # Field name made lowercase.
    idtallaproducto = models.ManyToManyField(Talla,)
    # Field name made lowercase.
    idgenero = models.ForeignKey(Genero, on_delete=models.CASCADE,)
    # Field name made lowercase.
    idmarca = models.ForeignKey(Marca, on_delete=models.CASCADE, )
    # Field name made lowercase.
    idcategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, )
    # Field name made lowercase.
    idtipoproducto = models.ForeignKey(Tipoproducto, on_delete=models.CASCADE)
    # Field name made lowercase.
    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='nombre')
    # Field name made lowercase.
    mostrarpaginicio = models.IntegerField(blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    state = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'producto'

    def __str__(self):
        return self.nombre


class Tipopago(models.Model):
    # Field name made lowercase.
    idtipopago = models.IntegerField(db_column='idTipoPago', primary_key=True)
    # Field name made lowercase.
    nomtipopago = models.CharField(db_column='nomTipoPago', max_length=50)

    def __str__(self):
        return self.nomtipopago

    class Meta:
        managed = True
        db_table = 'tipopago'


class Valoracion(models.Model):
    # Field name made lowercase.
    idvaloracion = models.IntegerField(
        db_column='id_Valoracion', primary_key=True)
    # Field name made lowercase.
    puntage = models.IntegerField(db_column='Puntage', blank=True, null=True)
    # Field name made lowercase.
    idprod = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'valoracion'


class Venta(models.Model):
    # Field name made lowercase.
    idventa = models.IntegerField(db_column='idVenta', primary_key=True)
    # Field name made lowercase.
    fechaventa = models.DateTimeField(db_column='fechaVenta')
    # Field name made lowercase.
    importeventa = models.FloatField(db_column='importeVenta')
    # Field name made lowercase.
    fechaentrega = models.DateTimeField(
        db_column='fechaEntrega', blank=True, null=True)
    # Field name made lowercase.
    direccionentrega = models.CharField(
        db_column='direccionEntrega', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    observacionentrega = models.CharField(
        db_column='observacionEntrega', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    estadoentrega = models.IntegerField(
        db_column='estadoEntrega', blank=True, null=True)
    # Field name made lowercase.
    observacionestadoentrega = models.CharField(
        db_column='observacionEstadoEntrega', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    idcliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, db_column='idCliente', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'venta'


class VentaProducto(models.Model):
    # Field name made lowercase.
    iddetalle = models.IntegerField(db_column='idDetalle', primary_key=True)
    cantidad = models.IntegerField()
    # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio')
    subtotal = models.IntegerField()
    descuento = models.IntegerField(blank=True, null=True)
    # Field name made lowercase.
    idprod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # Field name made lowercase.
    idventa = models.ForeignKey(
        Venta, on_delete=models.CASCADE, db_column='idVenta', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'venta_producto'
