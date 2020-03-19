from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django import forms

from .forms import ContactForm
from .models import Project_data, Category, project_tags, Tag, Project_pics
      
# Create your views here.

def create(request):
      
  if request.method == 'POST':
      filled_form = ContactForm(request.POST,request.FILES)
      if filled_form.is_valid():
            
            #create project
            new_project = Project_data.objects.create(
                  title = filled_form.cleaned_data['project_title'],
                  details = filled_form.cleaned_data['details'],
                  category = Category.objects.get(name = filled_form.cleaned_data['category']),
                  target = filled_form.cleaned_data['target'],
                  start_date = filled_form.cleaned_data['start_date'],
                  end_date = filled_form.cleaned_data['end_date'],
                  )
            
            #save all pictures
            for file in request.FILES.getlist('images'):
                  instance = Project_pics(
                        project = new_project,
                        image = file
                  )
                  instance.save()
                  
            #insert all tags
            for val in filled_form.cleaned_data['tags']:
                  project_tags.objects.create(
                        project = new_project,
                        tag_id = Tag.objects.get(name=val)
                  )
            return redirect(f"/project/{new_project.id}")
      return render(request, 'project/create.html', {'form': filled_form})
            
  else:
      form = ContactForm()
      return render(request, 'project/create.html', {'form': form})
  
def project(request):
    context = {
        "images": ["https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRXzoLYuz49nb6hd68DgWT7zFBxe5E81268lhh94dIMnyzRzNQM","https://i.insider.com/5d02563ddaa4821bf4575092?width=1100&format=jpeg&auto=webp","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRXzoLYuz49nb6hd68DgWT7zFBxe5E81268lhh94dIMnyzRzNQM"],
        "title": "this is a title",
        "details":
"""ou have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run python manage.py migrate to apply them.
March 18, 2020 - 13:34:36
Django version 3.0.4, using settings fundraiser.settings
Quit the server with CTRL-BREAK.
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run python manage.py migrate to apply them.
March 18, 2020 - 13:34:39
Django version 3.0.4, using settings fundraiser.settings""",
      "current":9000,
      "target":10000
    }
    return render(request,'project/project.html',context)
