import imp
from urllib.parse import urlparse
from django.urls import path
from home import views

# creating urls for homepage 
urlpatterns = [
    path('', views.home, name="home_page"),
    path('signup/',views.sign_up, name="signup"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.user_logout, name="user_logout"),
]
