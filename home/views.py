from django.shortcuts import render
from random import shuffle
from project.models import Project_data, Category, project_tags,  Project_pics
from django.db.models import Q
from user.models import Profile

# Create your views here.


def home(request):
    latest_projects = Project_data.objects.order_by('-created_at')[:3]
    featured_projects = list(Project_data.objects.filter(featured=True))
    categories = list(Category.objects.all())
    shuffle(categories)
    shuffle(featured_projects)

    context = {
        "latest_projects": latest_projects,
        "featured_projects": featured_projects[:3],
        "categories": categories[:3],
    }

    return render(request, 'home/home.html', {"context": context})


def categories(request):

    projects = Project_data.objects.all()
    categories = Category.objects.all()


    context = {
        "projects": projects,
        "categories": categories,
    }

    return render(request, 'home/categories.html', {"context": context})


def search(request):
    q = request.GET.get("q")
    projects = Project_data.objects.filter(Q(title__icontains=q)|Q(tags__tag__icontains=q))

    return render(request, 'home/search.html', {"projects": projects})


def contact(request):
    user = Profile.objects.get(user_id=request.session['logged_in_user'])
    return render(request, 'home/contact.html')