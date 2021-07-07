from django.shortcuts import redirect
from django.urls.base import reverse
import re

def usuario_group_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        if request.user.is_authenticated:
            grupo=request.user.groups.all()
            if request.user.is_superuser & request.user.is_staff:
                return response
            if grupo[0].name == 'Usuario':
                if re.search('producto/[0-9]+/edit',request.path):
                    return redirect('catalog:index')
                elif re.search('producto/[0-9]+/delete',request.path):
                    return redirect('catalog:index')
                else:
                    pass
            if grupo[0].name == 'Moderador':
                if 'carrito/' in request.path:
                    return redirect('catalog:index')
        return response

    return middleware