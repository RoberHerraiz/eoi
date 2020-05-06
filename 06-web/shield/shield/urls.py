"""shield URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import commons.views
import metahumans.views

urlpatterns = [

    path('', commons.views.homepage),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('metahumans/', metahumans.views.list_all_metahumans),
    path('teams/', metahumans.views.list_all_teams),
=======
    path('metahumans/', metahumans.views.list_all_metahumans), 
    path('teams/', metahumans.views.list_all_teams), 
>>>>>>> e428c7a107ee62527848e4e4586cfbb34e7f6d16
]
