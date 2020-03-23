from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in', )
]