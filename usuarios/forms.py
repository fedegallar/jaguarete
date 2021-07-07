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
        fields=['username', 'first_name', 'last_name', 'email', 'cuilcuit', 'telefono', 'domicilio', 'ciudad', 'provincia']
    
    def clean(self):
        cleaned_data = super(NewUserForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        password = cleaned_data.get('password')
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        cuilcuit = cleaned_data.get('cuilcuit')
        email = cleaned_data.get('email')
        telefono = cleaned_data.get('telefono')
        domicilio = cleaned_data.get('domicilio')
        ciudad = cleaned_data.get('ciudad')
        provincia = cleaned_data.get('provincia')
        if confirm_password != password:
            self.add_error('password', "Las contraseñas no coinciden")
        if not username:
            self.add_error('username', "username no puede estar vacio")
        if not first_name:
            self.add_error('first_name', "Nombres no puede estar vacío.")
        if not last_name:
            self.add_error('last_name', "Apellidos no puede estar vacio.")
        if not cuilcuit:
            self.add_error('cuilcuit', "CUIL/CUIT no puede estar vacio.")
        if not email:
            self.add_error('email', "Correo no puede estar vacio.")
        if not telefono:
            self.add_error('telefono', "Telefono no puede estar vacio.")
        if not domicilio:
            self.add_error('domicilio', "Domicilio no puede estar vacio.")
        if not ciudad:
            self.add_error('ciudad', "Ciudad no puede estar vacio.")
        if not provincia:
            self.add_error('provincia', "Provincia no puede estar vacio.")
        return cleaned_data

class EditUserForm(ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    confirm_password=forms.CharField(label='Confirmar contraseña' ,widget=forms.PasswordInput())
    class Meta:
        model=Usuario
        fields=['first_name', 'last_name', 'email', 'cuilcuit', 'telefono', 'domicilio', 'ciudad', 'provincia']
    
    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        confirm_password = cleaned_data.get('confirm_password')
        password = cleaned_data.get('password')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        cuilcuit = cleaned_data.get('cuilcuit')
        email = cleaned_data.get('email')
        telefono = cleaned_data.get('telefono')
        domicilio = cleaned_data.get('domicilio')
        ciudad = cleaned_data.get('ciudad')
        provincia = cleaned_data.get('provincia')
        if confirm_password != password:
            self.add_error('password', "Las contraseñas no coinciden")
        if not first_name:
            self.add_error('first_name', "Nombres no puede estar vacío.")
        if not last_name:
            self.add_error('last_name', "Apellidos no puede estar vacio.")
        if not cuilcuit:
            self.add_error('cuilcuit', "CUIL/CUIT no puede estar vacio.")
        if not email:
            self.add_error('email', "Correo no puede estar vacio.")
        if not telefono:
            self.add_error('telefono', "Telefono no puede estar vacio.")
        if not domicilio:
            self.add_error('domicilio', "Domicilio no puede estar vacio.")
        if not ciudad:
            self.add_error('ciudad', "Ciudad no puede estar vacio.")
        if not provincia:
            self.add_error('provincia', "Provincia no puede estar vacio.")
        return cleaned_data




class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(label='Contraseña', max_length=50, widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    email = forms.CharField(label='Dirección de correo', max_length=50, widget=forms.EmailInput)