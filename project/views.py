from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django import forms
from django.contrib import messages

from .forms import ContactForm
from .models import Project_data, Category, project_tags,  Project_pics
      
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
                  
            tags_list = request.POST.get('test').split(',')
            #insert all tags
            for val in tags_list:
                  project_tags.objects.create(
                        project = new_project,
                        tag = val
                  )
            return redirect(f"/project/{new_project.id}")
      return render(request, 'project/create.html', {'form': filled_form})
            
  else:
      form = ContactForm()
      return render(request, 'project/create.html', {'form': form})
  
def project(request,project_id):
      pics=[]
      try:
            project = Project_data.objects.get(id=project_id)
            images = Project_pics.objects.filter(project_id=project_id)
            for i in images:
                  pics.append(i.image)
            context = {
                  "images": pics,
                  "project":project
            }
            print(context)
      except Project_data.DoesNotExist:
            return redirect(f'/project/error')
      return render(request,'project/project.html',context)

      
def error(request):
      return render(request,"project/error.html")

def donate(request,project_id):
      if request.method == 'POST':
            project = Project_data.objects.get(id=project_id)
            project.current_money += int(request.POST.get('donation_value'))
            print(project.current_money, " === ",project.target)
            if project.current_money <= project.target:
                  project.save()
                  messages.success(request, 'Your Donation done successfully!')
                  return redirect(f"/project/{project_id}")
            else:
                  messages.error(request, 'Your Donation failed')
                  return redirect(f"/project/{project_id}")
      else:
            return redirect(f"/project/{project_id}")
