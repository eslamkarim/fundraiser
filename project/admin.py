from django.contrib import admin
from .models import Project_data, Category, Tag, project_tags, Project_pics, project_comments


# Register your models here.

admin.site.register(Project_data)
admin.site.register(project_tags)
admin.site.register(Project_pics)
admin.site.register(project_comments)
admin.site.register(Tag)
admin.site.register(Category)