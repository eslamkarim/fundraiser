from django.urls import path,include
from .views import create, project, donate

urlpatterns = [
    path('create/', create, name='create'),
    path('', project),
    path('<int:project_id>/donate/',donate, name='donate'),
]
