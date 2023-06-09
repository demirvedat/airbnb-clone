"""airbnb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from appMy.views import *
from appUser.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index, name='Index'),
    path('home/<id>/',Index, name='Index'),
    path('detail/<id>/',Detail, name='Detail'),
    path('profile/<str:pk>',Profile, name='Profile'),
    path('sharehome/',Sharehome, name='Sharehome'),
    path('homeadd/',Homeadd, name='Homeadd'),
    
    # Userpart
    path('login/',loginUser,name='loginUser'),
    path('register/',registerUser,name='registerUser'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
