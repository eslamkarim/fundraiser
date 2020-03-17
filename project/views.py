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
  