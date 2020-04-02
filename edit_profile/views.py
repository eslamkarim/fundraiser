from django.shortcuts import render
from project.models import Project_data, Category, project_tags,  Project_pics
from user_profile.models import User


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
        project = Project_data.objects.all()
        # user = User.objects.all()[:1].get()
        user = User.objects.get(user_id=1)
        dic = {"p_data": project,
                 "data": user}
        return render(request, "edit_profile/edit_profile.html", dic)

