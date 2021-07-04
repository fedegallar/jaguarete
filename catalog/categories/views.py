from catalog.models import Category
from django.shortcuts import redirect, render, get_object_or_404
from .forms import CategoryForm

def category_delete(request):
    categories = Category.objects.all()
    return render(request, "catalog/categories.html", {"categories": categories})

def category_new(request):
    categoryForm = CategoryForm
    return render(request, "catalog/categories/form.html", {"categoryForm": categoryForm})

def category_edit(request, id):
    if request.method == 'PUT':
        categoryForm = CategoryForm(instance=request.PUT)
        categoryForm.save()
    category = get_object_or_404(Category, pk=id)
    categoryForm = CategoryForm(instance=category)
    return render(request, "catalog/categories/form.html", {"categoryForm": categoryForm})