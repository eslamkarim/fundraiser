from django.urls import path,include
from .views import create, project, donate, error, comment, report, rate, reply, report_comment, cancel_project

urlpatterns = [
    path('create/', create, name='create'),
    path('<int:project_id>', project, name='project'),
    path('<int:project_id>/donate/',donate, name='donate'),
    path('<int:project_id>/comment/',comment, name='comment'),
    path('<int:project_id>/report/',report, name='report'),
    path('<int:project_id>/cancel/',cancel_project, name='cancel_project'),
    path('<int:project_id>/report_comment/<int:comment_id>',report_comment, name='report_comment'),
    path('<int:project_id>/rate/',rate, name='rate'),
    path('<int:project_id>/<int:comment_id>/reply/',reply, name='reply'),
    path('error', error)

]
