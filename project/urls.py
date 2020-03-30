from django.urls import path,include
from .views import create, project, donate, error, comment

urlpatterns = [
    path('create/', create, name='create'),
    path('<int:project_id>', project, name='project'),
    path('<int:project_id>/donate/',donate, name='donate'),
    path('<int:project_id>/comment/',comment, name='comment'),
    path('error', error)

]
