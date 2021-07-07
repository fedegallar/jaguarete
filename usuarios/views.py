from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import Group
from django.urls.base import reverse
from .forms import NewUserForm, EditUserForm, LoginForm, ForgotPasswordForm
from .models import Usuario

# Create your views here.

def login(request):
    loginForm = LoginForm
    if  request.user.is_authenticated:
        return redirect(reverse('catalog:index'))
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)    
                return redirect(reverse('catalog:index'))
            else:
                return render(request, 'usuarios/login.html',{'loginform': loginForm})
        else:
            return render(request, 'usuarios/login.html',{'loginform': loginForm})        

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect(reverse('catalog:index'))
    else:
        return redirect(reverse('catalog:index'))

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('catalog:index'))
    else:
        if request.method == 'POST':
                registerForm = NewUserForm(request.POST)
                if registerForm.is_valid():
                    password = registerForm.cleaned_data['password']
                    username = registerForm.cleaned_data['username']
                    first_name = registerForm.cleaned_data['first_name']
                    last_name = registerForm.cleaned_data['last_name']
                    cuilcuit = registerForm.cleaned_data['cuilcuit']
                    email = registerForm.cleaned_data['email']
                    telefono = registerForm.cleaned_data['telefono']
                    domicilio = registerForm.cleaned_data['domicilio']
                    ciudad = registerForm.cleaned_data['ciudad']
                    provincia = registerForm.cleaned_data['provincia']
                    usuario = Usuario(username=username, first_name=first_name, last_name=last_name,
                    cuilcuit=cuilcuit, email=email, telefono=telefono, domicilio=domicilio, ciudad=ciudad, provincia=provincia, is_active=True)
                    usuario.set_password(password)
                    usuario.save()
                    usuario_group = Group.objects.get(name='Usuario')
                    usuario.groups.add(usuario_group)
                    usuario.save()
                    return redirect(reverse('usuarios:login'))
                else:
                    return render(request, 'usuarios/register.html',{'registerForm': registerForm})
        else:
            registerForm = NewUserForm
            return render(request, 'usuarios/register.html',{'registerForm': registerForm})
    
def edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            editForm = EditUserForm(request.POST, instance=request.user)
            if editForm.is_valid():
                editForm.save()
                return render(request, 'usuarios/edit.html',{'editForm': editForm, 'message': 'Usuario editado.'})
        else:
            editForm = EditUserForm(instance=request.user)
            return render(request, 'usuarios/edit.html',{'editForm': editForm})
    else:
        return redirect(reverse('catalog:index'))
    
def forgot_password(request):
    forgotPasswordForm = ForgotPasswordForm
    return render(request, 'usuarios/forgot_password.html',{'forgotPasswordForm': forgotPasswordForm})
    