from django.shortcuts import render

# Create your views here.
def user_edit (request,id):
    user =User.objects.get(id=id)
    # args ={'user':request.user}
    return render(request,'user-profile/user-profile.html',{'user_data':user})
