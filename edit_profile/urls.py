from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.user_view,name="edit"),
    path('save', views.user_edit, name="user_edit"),
]