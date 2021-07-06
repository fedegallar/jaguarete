from catalog.models import Product
from django.db import models
from usuarios.models import Usuario
from catalog.models import Product
# Create your models here.

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    carrito_productos = models.ManyToManyField(Product, through='CarritoProducto')

    def getProductosList(self):
        return CarritoProducto.objects.filter(carrito=self)
        
    


class CarritoProducto(models.Model):
     carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.IntegerField(verbose_name='Cantidad', default=0)