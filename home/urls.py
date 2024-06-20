from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name='home'),
    path("service", views.service, name='service'),
    path("login", views.login, name='login'),  
    path("signup", views.signup, name='signup')
]
