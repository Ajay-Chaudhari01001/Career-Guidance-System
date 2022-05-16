"""FindMyCareer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from msvcrt import LK_NBLCK
from django.contrib import admin
from django.urls import path
from home import views
from predict import views as pv
from educards import views as ev
from loginsystem import views as lv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home"),
    path('signup/',lv.sign_up, name="signup"),
    path('login/', lv.user_login, name="login"),
    path('profile', lv.user_profile, name="profile"),
    path('logout/', lv.user_logout, name="user_logout"),
    path('changepass/', lv.user_change_pass, name="changepass"),
    path('contact/', views.user_contact, name="contact"),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('after10th/', ev.after10th, name="after10th"),
    path('after12th/', ev.after12th, name="after12th"),
    path('aftergraduation/', ev.aftergraduation, name="aftergraduation"),
    path("prediction/", pv.question_form, name="predict"),
]

