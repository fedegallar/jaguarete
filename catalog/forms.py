from django.forms.models import ModelForm

from .models import Product, Category

CATEGORIES = Category.objects.all()


class ProductForm(ModelForm):

    class Meta:
        model=Product
        fields=['title','description','image','category','price','stock']