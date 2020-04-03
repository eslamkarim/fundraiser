from django.shortcuts import render,redirect
from project.models import Project_data, Category, project_tags,  Project_pics
from user.models import Profile
import re
from datetime import datetime

def check_phone(mobile_phone):
    matcher = re.search('^(010|011|015|012)([0-9]{8})', mobile_phone)
    if matcher:
        return True
    return False


def check_empty(first_name):
    if first_name == '' :
        return False
    return True

# Create your views here.
# def user_edit (request):
    # if request.method =='POST':
    #     form=UserChangeForm(request.POST,instance=request.user)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/profile')
    # else:
    #     form=UserChangeForm(instance=request.user)
    #     args={'form':form}
    #     return render(request,'edit_profile/edit_profile.html',args)

def user_view(request):
    if 'logged_in_user' in request.session:
        project = Project_data.objects.filter(user_id =request.session['logged_in_user'])
        user = Profile.objects.get(user_id=request.session['logged_in_user'])
        dic = {"p_data": project,
                 "data": user}
        return render(request, "edit_profile/edit_profile.html", dic)
    else:
        return redirect(f"sign_in")

def user_edit(request):
    user_id=request.session['logged_in_user']

    if request.method == 'POST':
            dict={}
            first_name=request.POST.get("first_name")
            if  check_empty(first_name):
               dict['user_first_name']=first_name
            last_name = request.POST.get("last_name")
            if  check_empty(last_name):
                dict['user_last_name'] = last_name
            phone_number = request.POST.get("phone_number")
            if check_phone(phone_number):
                dict['user_phone_number'] = phone_number
            birth_date=request.POST.get("birth_date")
            if  check_empty(birth_date):
                dict['user_birthDate'] = birth_date
            country= request.POST.get('country')
            if check_empty(country):
                dict['user_country'] = country
            Profile.objects.filter(user_id=user_id).update(**dict)


            return redirect (f"/profile/")

    else:
            return render(request, 'edit_profile/edit_profile.html')




