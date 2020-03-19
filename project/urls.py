from django.urls import path,include
from .views import create,project

urlpatterns = [
    path('create/', create,name='create'),
    path('', project),
]
