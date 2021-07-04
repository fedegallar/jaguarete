from django import forms
from django.forms.models import ModelForm

from .models import Product, Category

CATEGORIES = Category.objects.all()


class ProductForm(ModelForm):

    class Meta:
        model=Product
        fields=['title','description','image','category','price','stock']
    
class AddToCarritoForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    cantidad_producto = forms.IntegerField(label='Cantidad')
