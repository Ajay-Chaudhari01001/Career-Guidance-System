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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('signup/', include('home.urls')),
    path('login/', include('home.urls')),
    path('profile/', include('home.urls')),
    path('logout/', include('home.urls')),
    path('changepass/', include('home.urls')),
    path('contact/', include('home.urls')),
    path('aboutUs/', include('home.urls')),
    path('after10th/', include('home.urls')),
    path('after12th/', include('home.urls')),
    path('aftergraduation/', include('home.urls')),
    path('givetestinfo/', include('home.urls')),
    # path('sendmail/', include('home.urls')),
    path('footer/', include('home.urls')),
]
