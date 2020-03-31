from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('categories', views.categories),
    path('search', views.search),
]