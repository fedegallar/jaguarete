from carrito.forms import EditQuantityItemCarrito
from django.http.response import HttpResponse, JsonResponse
from django.middleware.csrf import get_token
from django.urls.base import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from .models import Carrito, CarritoProducto
from catalog.models import Product

# Create your views here.

def index(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
        carrito_productos = CarritoProducto.objects.filter(carrito=carrito)
        total = 0
        for cp in carrito_productos:
            total += cp.product.price * cp.quantity
        return render(request, 'carrito/index.html', {'carritoProductos': carrito_productos, 'total': total, 'vacio': False})
    except Carrito.DoesNotExist:
        return render(request, 'carrito/index.html', {'vacio': True})


def AddProductoToCarrito(request):
    if request.method == "POST":
        try:
            carrito = Carrito.objects.get(usuario=request.user)
        except Carrito.DoesNotExist:
            carrito = Carrito(usuario=request.user)
            carrito.save()
            carrito = Carrito.objects.get(usuario=request.user)
        finally:
            cantidad = request.POST['cantidad_producto']
            productId = request.POST['id']
            producto = Product.objects.get(pk=productId)
            producto_carrito = CarritoProducto(carrito = carrito, product= producto, quantity=cantidad)
            producto_carrito.save()
            return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect(reverse('catalog:index'))

def EditProductoFromCarrito(request, id):
    producto_carrito = CarritoProducto.objects.get(pk=id)
    if request.method == 'POST':
        producto_carrito.id = request.POST['id']
        producto_carrito.quantity = request.POST['cantidad_producto']
        producto_carrito.save()
        return redirect(reverse('carrito:index'))
    else:
        csrf_token = get_token(request)
        csrf_token_html = '<input type="hidden" name="csrfmiddlewaretoken" value="{}" />'.format(csrf_token)
        editform = EditQuantityItemCarrito(initial={'id':producto_carrito.id, 'cantidad_producto': producto_carrito.quantity})
        html = render_to_string('carrito/edit.html',{'editform':editform, 'id':id, 'csrf_token':csrf_token})
        return HttpResponse(html)


def RemoveProductoFromCarrito(request, id):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
        carritoProducto = get_object_or_404(CarritoProducto, pk=id)
        carritoProducto.delete()
        productListCarrito = CarritoProducto.objects.filter(carrito=carrito)
        if len(productListCarrito) == 0:
            carrito.delete()
            return redirect(reverse('carrito:index'))
        return JsonResponse({'message': 'Se ha eliminado un item del carrito.'})
    except Carrito.DoesNotExist:
        return JsonResponse({'message':'Ha ocurrido un error, intente mas tarde.'})


