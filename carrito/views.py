from django.urls.base import reverse
from usuarios.models import Usuario
from django.shortcuts import redirect, render, get_object_or_404
from .models import Carrito, CarritoProducto
from catalog.models import Product

# Create your views here.


def AddProductoToCarrito(request):
    if request.method == "POST":
        carrito = Carrito.objects.get(usuario=request.user)
        if carrito is None:
            carrito = Carrito(usuario=request.user)
            carrito.save()
            carrito = Carrito.objects.get(usuario=request.user)
            cantidad = request.POST['cantidad_producto']
            productId = request.POST['id']
            producto = Product.objects.get(pk=productId)
            producto_carrito = CarritoProducto(carrito = carrito, product= producto, quantity=cantidad)
            producto_carrito.save()
        else:
            cantidad = request.POST['cantidad_producto']
            productId = request.POST['id']
            producto = Product.objects.get(pk=productId)
            producto_carrito = CarritoProducto(carrito = carrito, product= producto, quantity=cantidad)
            producto_carrito.save()
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(reverse('catalog:index'))


def RemoveProductoFromCarrito():
    pass

