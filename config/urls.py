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

from thapp import views as viewsth
from jeapp import views as viewsje
from mgapp import views as viewsmg
from mainapp import views as viewsm

urlpatterns = [
    ### mainapp (http://127.0.0.1:8000/)
    path('', include('mainapp.urls')),
    path('main/', include('mainapp.urls')),
    
    ### thapp (http://127.0.0.1:8000/th/)
    path('th/', include('thapp.urls')),
    
    ### thapp (http://127.0.0.1:8000/th/)
    path('je/', include('jeapp.urls')),
    
    ### thapp (http://127.0.0.1:8000/mg/)
    path('mg/', include('mgapp.urls')),
    
    path('admin/', admin.site.urls),

]
