from django.contrib import admin
from project.models import Project_data, Category, project_tags, Project_pics, project_comments



# Register your models here.

admin.site.register(Project_data)
admin.site.register(project_tags)
admin.site.register(Project_pics)
admin.site.register(project_comments)
admin.site.register(Category)