from django.shortcuts import render
from random import shuffle
from project.models import Project_data, Category, project_tags,  Project_pics

# Create your views here.


def home(request):
    latest_projects = Project_data.objects.order_by('-created_at')[:3]
    featured_projects = Project_data.objects.order_by('-rating')[:3]
    categories = list(Category.objects.all())
    shuffle(categories)

    context = {
        "latest_projects": latest_projects,
        "featured_projects": featured_projects,
        "categories": categories[:3]
    }

    return render(request, 'home/home.html', {"context": context})

def categories(request):
    projects = Project_data.objects.all()
    categories = Category.objects.all()

    context = {
        "projects": projects,
        "categories": categories
    }

    return render(request, 'home/categories.html', {"context": context})