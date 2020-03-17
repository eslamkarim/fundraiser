from django.shortcuts import render

# Create your views here.
def project(request):
    context = {
        "images": ["https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRXzoLYuz49nb6hd68DgWT7zFBxe5E81268lhh94dIMnyzRzNQM","https://i.insider.com/5d02563ddaa4821bf4575092?width=1100&format=jpeg&auto=webp","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRXzoLYuz49nb6hd68DgWT7zFBxe5E81268lhh94dIMnyzRzNQM"]
    }
    return render(request,'project/project.html',context)