from django.shortcuts import render
from random import shuffle






from project.models import Project_data, Category, project_tags,  Project_pics

# Create your views here.


def home(request):
    # latest_projects = Project_data.objects.order_by('-created_at')[:5]
    featured_projects = Project_data.objects.order_by('-rating')[:5]
    categories = list(Category.objects.all())
    shuffle(categories)

    context = {
        # "latest_projects": latest_projects,
        "featured_projects": featured_projects,
        "categories": categories[:3]
    }

    return render(request, 'home/home.html', {"context": context})
