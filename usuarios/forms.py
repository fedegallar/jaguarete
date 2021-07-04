from typing import Type
from django import forms
from django.forms import widgets
from django.forms.forms import Form
from django.forms.models import ModelForm

from .models import Usuario


class NewUserForm(ModelForm):

    class Meta:
        model=Usuario
        fields='__all__'

class EditUserForm(ModelForm):

    class Meta:
        model=Usuario
        fields=['password', 'first_name', 'last_name', 'email', 'cuilcuit', 'telefono', 'domicilio', 'ciudad', 'provincia']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(label='Contraseña', max_length=50, widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    email = forms.CharField(label='Dirección de correo', max_length=50, widget=forms.EmailInput)