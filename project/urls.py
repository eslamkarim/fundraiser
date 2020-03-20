from django.urls import path,include
from .views import create, project, donate, error

urlpatterns = [
    path('create/', create, name='create'),
    path('<int:project_id>', project),
    path('<int:project_id>/donate/',donate, name='donate'),
    path('error', error)

]
