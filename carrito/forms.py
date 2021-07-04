from django import forms
from django.forms.models import ModelForm

class AddToCarritoForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    cantidad_producto = forms.IntegerField(label='Cantidad')