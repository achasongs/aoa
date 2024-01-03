from django.contrib import admin
from django.urls import path, include
from .views import mainapp, connect, about


urlpatterns = [
    path('', mainapp, name="home"),
    path('connect/', connect, name="connect"),
    path('about/', about, name="about"),
]