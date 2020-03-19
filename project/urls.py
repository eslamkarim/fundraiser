from django.urls import path,include
from .views import create,project,error

urlpatterns = [
    path('create/', create,name='create'),
    path('<int:project_id>', project),
    path('404',error),
]
