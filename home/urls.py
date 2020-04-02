from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.categories),
    path('search', views.search),
    path('contact', views.contact),
    path('', views.home, name="home"),
]