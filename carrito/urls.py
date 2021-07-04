from django.urls import path
from .views import AddProductoToCarrito, index

app_name="carrito"

urlpatterns = [
    path('', index, name='index'),
    path('addProductToCarrito', AddProductoToCarrito, name='AddProductToCarrito')   
]
