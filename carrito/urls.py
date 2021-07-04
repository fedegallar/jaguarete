from django.urls import path
from .views import AddProductoToCarrito

app_name="carrito"

urlpatterns = [
 path('addProductToCarrito', AddProductoToCarrito, name='AddProductToCarrito')   
]
