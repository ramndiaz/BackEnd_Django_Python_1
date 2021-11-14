"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from project1.views import hello, bye, dameFecha, calculaEdad, home #el metodo que creamos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('bye/', bye),
    path('home/', home),
    path('date/', dameFecha),
    path('edad/<int:nacim>, <int:agno>', calculaEdad) #indicamos que vamos a recibir 2 parametros y que los vuelva enteros
]
