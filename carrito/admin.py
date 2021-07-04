from django.contrib import admin
from .models import Carrito, CarritoProducto

class CarritoAdmin(admin.ModelAdmin):
    pass


class CarritoProductoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Carrito, CarritoAdmin)
admin.site.register(CarritoProducto, CarritoProductoAdmin)

# Register your models here.
