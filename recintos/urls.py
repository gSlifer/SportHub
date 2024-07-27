"""
URL configuration for recintos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from recintosapp.views import register_user,login_user,logout_user,recintos, index, agregar_recinto, recintos_details, rating, recintos_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('recintos/', recintos, name='recintos'),
    path('recintos/<int:id>/', recintos_details, name='recintos_details'),
    path('agregar_recinto/', agregar_recinto, name='agregar_recinto'),
    path('agregar_rating/<int:id>/', rating, name='agregar_valoracion'),
    path('api/recintos/', recintos_api, name='recintos_api')
]
