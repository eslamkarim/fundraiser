from django.shortcuts import render
from random import shuffle
from project.models import Project_data, Category, project_tags,  Project_pics
from django.contrib.auth.models import User

# Create your views here.
#
# def userProfile(request):#id
#  #   user=Users.objects.get(id=id)
#     user={"id":1,"name":"samar mahmoud","phone":"011455","mail":"samar@yahoo.com","country":"Egypt","facebook":"www.facebook.com"}
#     args={"data":user}
#     return render(request,'user-profile/user-profile.html',args)


def userProject(request,id):
    project = Project_data.objects.get(id=id)
    # dic = {"p_data": project}
    return render(request, "user-profile/user-profile.html", {"p_data": project})

def userProfile (request,id):
    user =User.objects.get(id=id)
    # args ={'user':request.user}
    return render(request,'user-profile/user-profile.html',{'user_data':user})

