import imp
from urllib.parse import urlparse
from django.urls import path
from home import views

# creating urls for homepage 
urlpatterns = [
    path('', views.home),
    path('signup/',views.sign_up),
    path('login/', views.login),
]
