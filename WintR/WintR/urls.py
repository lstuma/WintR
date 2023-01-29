"""WintR URL Configuration

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
import WintR.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('login/', views.login_),
    path('logout/', views.logout_),
    path('signup/', views.signup),
    path('nextpage/', views.nextpage),
    path('post/', views.post),
    path('attend/', views.attend),
    path('user/', views.user),
    path('user/nextpage/', views.user_nextpage),
    path('tag/', views.tag),
    path('tag/nextpage/', views.tag_nextpage)
]
