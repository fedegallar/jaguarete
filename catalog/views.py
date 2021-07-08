from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Category, Product
from .forms import NewProductForm, EditProductForm
from carrito.forms import AddToCarritoForm
# Create your views here.


def index(request):
    products = Product.objects.order_by("-pk")[:10]
    main_products = products[:3]
    second_products = products[4:10]
    return render(request, "catalog/index.html", {"main_products": main_products, "second_products": second_products})

def find_by_category(request, idCategory):
    category = Category.objects.get(pk=idCategory)
    products = Product.objects.filter(category=category).order_by("-pk")[:10]
    main_products = products[:3]
    second_products = products[4:10]
    return render(request, "catalog/index.html", {"main_products": main_products, "second_products": second_products})

def find_by_title(request):
    search = request.GET.get('search')
    products = Product.objects.filter(title__contains=search).order_by("-pk")[:10]
    main_products = products[:3]
    second_products = products[4:10]
    return render(request, "catalog/index.html", {"main_products": main_products, "second_products": second_products})

def view_product(request, id):
    product = Product.objects.get(id=id)
    addToCarritoForm = AddToCarritoForm(initial={'id':id})
    return render(request, "catalog/view.html", {'product': product,'addToCarritoForm': addToCarritoForm })

def new_product(request):
    if request.method == 'POST':
        productForm = NewProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
            return HttpResponseRedirect(reverse('catalog:index'))
        print(productForm.errors)
        return redirect(reverse('catalog:new-product'))
    else:
        form = NewProductForm
        return render(request, "catalog/new.html", {"formulario": form})


def edit(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        producto = Product.objects.get(id=id)
        editform = EditProductForm(request.POST, request.FILES, instance=producto)
        if editform.is_valid():
            editform.save()
            return render(request, "catalog/edit.html", {'id':product.id, "formulario":editform, "title": f'Editar {product.category} - {product.title}(Guardado)'})
        return render(request, "catalog/edit.html", {'id':product.id, "formulario":editform, "title": f'Editar {product.category} - {product.title}(Error)'}) 
    else:
        editform = EditProductForm(instance=product)
        return render(request, "catalog/edit.html", {'id':product.id, "formulario": editform, "title": f'Editar {product.category} - {product.title}'})


def delete_product(request, id):
    product_delete = get_object_or_404(Product, pk=id)
    title = product_delete.title
    product_delete.delete()
    return redirect(reverse('catalog:index'))

def about(request):
    return render(request, "catalog/about.html", {})