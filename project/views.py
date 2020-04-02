from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django import forms
from django.contrib import messages
from itertools import chain

from .forms import ContactForm
from .models import Project_data, Category, project_tags,  Project_pics, project_comments, Report_project, Donate_project, Rate_project, project_comment_replies, Report_comment
from user.models import User
# Create your views here.


def create(request):
    # del request.session['logged_in_user']
    # print(request.session['logged_in_user'])
    if request.method == 'POST':
        filled_form = ContactForm(request.POST, request.FILES)
        if filled_form.is_valid():
            print("===============")
            print(request.FILES.getlist('cover_images')[0])
            # create project
            new_project = Project_data.objects.create(
                title=filled_form.cleaned_data['project_title'],
                details=filled_form.cleaned_data['details'],
                category=Category.objects.get(
                    name=filled_form.cleaned_data['category']),
                target=filled_form.cleaned_data['target'],
                start_date=filled_form.cleaned_data['start_date'],
                end_date=filled_form.cleaned_data['end_date'],
                cover=request.FILES.getlist('cover_images')[0],
                user_id=request.session['logged_in_user']
            )

            # save all pictures
            for file in request.FILES.getlist('images'):
                instance = Project_pics(
                    project=new_project,
                    image=file
                )
                instance.save()

            tags_list = request.POST.get('test').split(',')
            # insert all tags
            for val in tags_list:
                project_tags.objects.create(
                    project=new_project,
                    tag=val
                )
            return redirect(f"/project/{new_project.id}")
        print(filled_form.errors)
        return render(request, 'project/create.html', {'form': filled_form})
    else:
        if 'logged_in_user' in request.session:
        	form = ContactForm()
        	return render(request, 'project/create.html', {'form': form})
        else:
            return render(request, 'user/sign_in.html')


def project(request, project_id):
    pics = []
    try:
        project = Project_data.objects.get(id=project_id)
        images = Project_pics.objects.filter(project_id=project_id)
        for i in images:
            pics.append(i.image)
        project_all_tags = project_tags.objects.filter(
            project_id=project_id).values_list("tag", flat=True)
        test_list = list(project_all_tags)
        related_projects_id = project_tags.objects.filter(tag__in=test_list).distinct(
        ).exclude(project_id=project_id).values_list("project", flat=True)[:5]
        related_projects_data = Project_data.objects.filter(
            id__in=list(related_projects_id))

        # get project comments
        comments = project_comments.objects.filter(project_id=project_id)
        context = {
            "images": pics,
            "project": project,
            "comments": comments,
            "related_projects_list": related_projects_data
        }
        print(context)

    except Project_data.DoesNotExist:
        return redirect(f'/project/error')
    return render(request, 'project/project.html', context)


def error(request):
    return render(request, "project/error.html")

def donate(request,project_id):
      if request.method == 'POST':
            donating_value = int(request.POST.get('donation_value'))
            project = Project_data.objects.get(id=project_id)
            project.current_money += donating_value
            if project.current_money <= project.target:
                  project.save()
                  Donate_project.objects.create(
                        project = project,
                        user = User.objects.get(user_id= request.session['logged_in_user']),
                        value = donating_value
                  )
                  messages.success(request, 'Your Donation done successfully!', extra_tags='donate')
                  return redirect(f"/project/{project_id}")
            else:
                  messages.error(request, 'Your Donation failed', extra_tags='donate')
                  return redirect(f"/project/{project_id}")
      else:
            return redirect(f"/project/{project_id}")
        
def comment(request, project_id):
    if request.method == 'POST':
        try:
	        project = Project_data.objects.get(id=project_id)
	        comment = request.POST.get('comment')
	        if len(comment) > 0:
		        project_comments.objects.create(
			        project=project,
			        comment=comment,
			        comment_user_id=request.session['logged_in_user']
		        )
		        return redirect(f"/project/{project_id}")
	        else:
		        return redirect(f"/project/{project_id}")
        except:
	        messages.error(request, 'Please login first!!!', extra_tags='comment')
	        return redirect(f"/project/{project_id}")
    else:
        return redirect(f"/project/{project_id}")
            
def report(request,project_id):
      if request.method == 'POST':
            if len(list(Report_project.objects.filter(user_id= request.session['logged_in_user'],project_id= project_id))):
                  messages.error(request, 'Your cant report more than one', extra_tags='report')
                  return redirect(f"/project/{project_id}")
            else:
                  project = Project_data.objects.get(id=project_id)
                  project.reports += 1 
                  project.save()
                  Report_project.objects.create(
                        project = project,
                        user = User.objects.get(user_id= request.session['logged_in_user'])
                  )
                  messages.success(request, 'Your report done successfully!', extra_tags='report')
                  return redirect(f"/project/{project_id}")
      else:
            return redirect(f"/project/{project_id}")
      
def rate(request,project_id):
      if request.method == 'POST':
            if len(list(Rate_project.objects.filter(user_id= request.session['logged_in_user'],project_id= project_id))):
                  messages.error(request, 'Your cant rate more than one', extra_tags='rate')
                  return redirect(f"/project/{project_id}")
            else:
                  rating_value = int(request.POST.get('rating',-1))
                  if rating_value > 0 and rating_value < 6:
                        project = Project_data.objects.get(id=project_id)
                        project.rating = (int(request.POST.get('rating'))+project.rating)/2
                        project.save()
                        messages.success(request, 'Your rating done successfully!', extra_tags='rate')
                        Rate_project.objects.create(
                              project = project,
                              user = User.objects.get(user_id= request.session['logged_in_user']),
                              value = rating_value
                        )
                        return redirect(f"/project/{project_id}")
                  else:
                        messages.error(request, 'Your rating failed', extra_tags='rate')
                        return redirect(f"/project/{project_id}")
      else:
            return redirect(f"/project/{project_id}")

def reply(request, project_id, comment_id):
    if request.method == 'POST':
        try:
	        project = Project_data.objects.get(id=project_id)
	        comment = project_comments.objects.get(id=comment_id)
	        reply = request.POST.get('reply')
	        if len(reply) > 0:
		        project_comment_replies.objects.create(
			        reply=reply,
			        comment=comment,
			        reply_user_id=request.session['logged_in_user']
		        )
		        return redirect(f"/project/{project_id}")
	        else:
		        return redirect(f"/project/{project_id}")
        except:
	        messages.error(request, 'Please login first!!!', extra_tags='comment')
	        return redirect(f"/project/{project_id}")
    else:
        return redirect(f"/project/{project_id}")

		
def report_comment(request,project_id,comment_id):
      if request.method == 'POST':
            if len(list(Report_comment.objects.filter(user_id= request.session['logged_in_user'],comment_id= comment_id))):
                  messages.error(request, 'Your cant report same comment more than one', extra_tags='report_comment')
                  return redirect(f"/project/{project_id}")
            else:
                  comment = project_comments.objects.get(id=comment_id)
                  Report_comment.objects.create(
                        comment = comment,
                        user = User.objects.get(user_id= request.session['logged_in_user'])
                  )
                  messages.success(request, 'Your report done successfully!', extra_tags='report_comment')
                  return redirect(f"/project/{project_id}")
      else:
            return redirect(f"/project/{project_id}")
