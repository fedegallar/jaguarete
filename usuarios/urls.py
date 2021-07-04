from django.urls import path
from .views import login, logout, register, forgot_password, edit
app_name='usuarios'
urlpatterns = [
 path('login/', login, name='login'),
 path('logout/', logout, name='logout'),
 path('register/', register, name='register'),
 path('forgot_password/', forgot_password, name='forgot_password'),
 path('edit/', edit, name='edit'),
]