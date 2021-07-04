from django.urls import path
from django.urls.conf import include
from .views import index, new_product, edit_product,view_product , delete_product, find_by_title ,about
app_name='catalog'
urlpatterns = [
    path('', index, name="index"),
    path('about',about, name="about"),
    path('categorias', include('catalog.categories.urls'), name="category"),
    path('producto/nuevo', new_product, name='new-product'),
    path('producto/find/',find_by_title, name='find_by_title'),
    path('producto/<int:id>', view_product, name='view_product'),
    path('producto/<int:id>/edit', edit_product, name='edit_product'),
    path('producto/<int:id>/delete', delete_product, name="delete_product")
]