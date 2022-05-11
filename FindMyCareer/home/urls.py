import imp
from urllib.parse import urlparse
from django.urls import path
from home import views

# creating urls for homepage 
urlpatterns = [
    path('', views.home, name="home_page"),
    path('signup/',views.sign_up, name="signup"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.user_profile, name="profile"),
    path('logout/', views.user_logout, name="user_logout"),
    path('changepass/', views.user_change_pass, name="changepass"),
    path('contact/', views.user_contact, name="contact"),
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('after10th/', views.after10th, name="after10th"),
    path('after12th/', views.after12th, name="after12th"),
    path('aftergraduation/', views.aftergraduation, name="aftergraduation"),
    path('givetestinfo/', views.givetestinfo, name="givetestinfo"),
    # path('sendemail/', views.send_email, name="sendemail"),
    #  path('footer/', views.footer, name="givetestinfo"),
]
