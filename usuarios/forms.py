from typing import Type
from django import forms
from django.forms import widgets
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.utils import timezone

from .models import Usuario


class NewUserForm(ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    confirm_password=forms.CharField(label='Confirmar contraseña' ,widget=forms.PasswordInput())
    class Meta:
        model=Usuario
        fields=['first_name', 'last_name', 'email', 'cuilcuit', 'telefono', 'domicilio', 'ciudad', 'provincia']
    
    def clean(self):
        confirm_password = self.cleaned_data['confirm_password']
        original_password = self.cleaned_data['password']
        if confirm_password != original_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return confirm_password, original_password

class EditUserForm(ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    confirm_password=forms.CharField(label='Confirmar contraseña' ,widget=forms.PasswordInput())
    class Meta:
        model=Usuario
        fields=['first_name', 'last_name', 'email', 'cuilcuit', 'telefono', 'domicilio', 'ciudad', 'provincia']
    
    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        confirm_password = self.cleaned_data['confirm_password']
        original_password = self.cleaned_data['password']
        if confirm_password != original_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data




class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(label='Contraseña', max_length=50, widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    email = forms.CharField(label='Dirección de correo', max_length=50, widget=forms.EmailInput)