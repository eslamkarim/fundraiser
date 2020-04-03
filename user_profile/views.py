from django.shortcuts import render,redirect
from project.models import Project_data, Category, project_tags,  Project_pics
from user.models import User


# def userProfile(request):#id
#  #   user=Users.objects.get(id=id)
#     user={"id":1,"name":"samar mahmoud","phone":"011455","mail":"samar@yahoo.com","country":"Egypt","facebook":"www.facebook.com"}
#     args={"data":user}
#     return render(request,'user_profile/user_profile.html',args)


def userProfile(request):
    if 'logged_in_user' in request.session:
        user_id =request.session['logged_in_user']
        project = Project_data.objects.filter(user_id=user_id)
        user = User.objects.get(user_id=user_id)
        dic = {"p_data": project,
           "data":user}
        return render(request, "user_profile/user_profile.html", dic)
    else:
        return  redirect(f"sign_in")
