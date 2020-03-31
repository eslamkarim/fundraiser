from django.urls import path,include
from .views import create, project, donate, error, comment, report, rate

urlpatterns = [
    path('create/', create, name='create'),
    path('<int:project_id>', project, name='project'),
    path('<int:project_id>/donate/',donate, name='donate'),
    path('<int:project_id>/comment/',comment, name='comment'),
    path('<int:project_id>/report/',report, name='report'),
    path('<int:project_id>/rate/',rate, name='rate'),
    path('error', error)

]
