import datetime
from django.db import models



class Marca(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __unicode__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __unicode__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=140)
    imagen = models.ImageField(upload_to='imagenes', null=True) 
    descripcion = models.CharField(max_length=250, null=True)
    marca = models.ForeignKey(Marca, null=True, related_name='producto_marca')
    categoria = models.ForeignKey(Categoria, null=True, related_name='producto_categoria')
    precio = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __unicode__(self):
        return self.nombre


class Compra(models.Model):
    usuario = models.CharField(max_length=140,null=True)
    email = models.EmailField(null=True)
    tarjeta = models.CharField(max_length=16,null=True)
    direccion = models.CharField(max_length=250, null=True)
    telefono = models.CharField(max_length=40, null=True)
    producto = models.ManyToManyField(Producto)
    total = models.IntegerField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    comfirmada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __unicode__(self):
        return "%s - %s" % (self.usuario, self.fecha)                
