from django.urls import path
from .views import login, register

urlpatterns = [
    path('login.html/',login, name="login"),
    path('login.html/register.html/',register, name="register"),
]