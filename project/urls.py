from django.urls import path,include
from project.views import create

urlpatterns = [
    path('create/', create,name='create')
]
