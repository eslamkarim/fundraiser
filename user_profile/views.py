from django.shortcuts import render
from random import shuffle
from project.models import Project_data, Category, project_tags,  Project_pics

from user.models import User


# def userProfile(request):#id
#  #   user=Users.objects.get(id=id)
#     user={"id":1,"name":"samar mahmoud","phone":"011455","mail":"samar@yahoo.com","country":"Egypt","facebook":"www.facebook.com"}
#     args={"data":user}
#     return render(request,'user_profile/user_profile.html',args)


def userProfile(request):
    project = Project_data.objects.all()
    # user = User.objects.all()[:1].get()
    user = User.objects.get(user_id =1)
    dic = {"p_data": project,
           "data":user}
    return render(request, "user_profile/user_profile.html", dic)
