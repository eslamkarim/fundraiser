from django.shortcuts import render
#import for models

# Create your views here.

def userProfile(request):#id
 #   user=Users.objects.get(id=id)
    user={"id":1,"name":"samar mahmoud","phone":"011455","mail":"samar@yahoo.com","country":"Egypt","facebook":"www.facebook.com"}
    dic={"data":user}
    return render(request,'user-profile/user-profile.html',dic)

