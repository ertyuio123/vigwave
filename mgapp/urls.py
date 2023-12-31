"""config URL Configuration

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
### include : 각 앱에서 관리하는 urls.py 호출 시 사용
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    ### about (http://127.0.0.1:8000/mg/nav_test/)
    path('nav_test/', views.nav_test),
    ### about (http://127.0.0.1:8000/mg/nav/)
    path('nav/', views.nav),
    ### copy2 (http://127.0.0.1:8000/mg/copy2/)
    path('copy2/', views.copy2),
    ### about (http://127.0.0.1:8000/mg/copy/)
    path('copy/', views.copy),
    ### about (http://127.0.0.1:8000/about/)
    path('temp/', views.temp),
    ### about (http://127.0.0.1:8000/about/)
    path('about/', views.about),
    ### mainapp (http://127.0.0.1:8000/mg/home/)
    path('home/', views.index),
    ### mainapp (http://127.0.0.1:8000/mg/home2/)
    path('home2/', views.index2),
]
