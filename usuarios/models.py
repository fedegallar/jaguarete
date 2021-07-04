from django.db import models
from django.contrib.auth.models import AbstractUser, User
# Create your models here.

class Usuario(AbstractUser):
    username = models.CharField(max_length = 50, blank = False, unique=True)
    first_name =  models.CharField(max_length = 50, blank = False)
    last_name =  models.CharField(max_length = 50, blank = False)
    email = models.EmailField(verbose_name='Correo', blank=False)
    cuilcuit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=20)
    provincia = models.CharField(max_length=20)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'cuilcuit', 'telefono', 'domicilio', 'ciudad', 'provincia']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'