from django.contrib import admin
from django.urls import path,include
from dashboard import views

urlpatterns = [
   path('', views.home, name='home'),
   path('home',views.home, name='home'),
   path('dashboard', views.dashboard, name='dashboard'),

   ]