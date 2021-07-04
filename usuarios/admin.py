from usuarios.models import Usuario
from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Usuario, UsuarioAdmin)