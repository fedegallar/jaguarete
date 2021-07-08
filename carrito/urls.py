from django.urls import path
from .views import AddProductoToCarrito, DestroyCarrito, EditProductoFromCarrito, RemoveProductoFromCarrito, index

app_name="carrito"

urlpatterns = [
    path('', index, name='index'),
    path('addProductToCarrito', AddProductoToCarrito, name= 'AddProductToCarrito'),
    path('destroy', DestroyCarrito, name= 'destroy'),
    path('remove/<int:id>', RemoveProductoFromCarrito, name= 'remove'),
    path('edit/<int:id>', EditProductoFromCarrito, name= 'edit'),    
]
