from django import views
from django.contrib import admin
from django.urls import path
from login import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login',views.loginUser, name='login'),
    path('logout',views.logoutUser, name='logout')
   
   
]
