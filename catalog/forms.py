from django import forms
from django.forms.models import ModelForm

from .models import Product, Category

CATEGORIES = Category.objects.all()


class NewProductForm(ModelForm):

    class Meta:
        model=Product
        fields=['title','description','image','category','price','stock']

class EditProductForm(ModelForm):
    
    class Meta:
        model=Product
        fields=['title','description','image','category','price','stock']
