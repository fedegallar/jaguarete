from django.forms.models import ModelForm

from catalog.models import Category


class CategoryForm(ModelForm):

    class Meta:
        model=Category
        fields=['description']