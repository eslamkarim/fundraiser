from django.shortcuts import render

# Create your views here.
def project(request):
    context = {
        "images": ["https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg", "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRXzoLYuz49nb6hd68DgWT7zFBxe5E81268lhh94dIMnyzRzNQM","https://i.insider.com/5d02563ddaa4821bf4575092?width=1100&format=jpeg&auto=webp","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRXzoLYuz49nb6hd68DgWT7zFBxe5E81268lhh94dIMnyzRzNQM"],
        "title": "this is a title",
        "details":
"""ou have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run python manage.py migrate to apply them.
March 18, 2020 - 13:34:36
Django version 3.0.4, using settings fundraiser.settings
Quit the server with CTRL-BREAK.
Watching for file changes with StatReloader
Performing system checks...
System check identified no issues (0 silenced).
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run python manage.py migrate to apply them.
March 18, 2020 - 13:34:39
Django version 3.0.4, using settings fundraiser.settings""",
      "current":9000,
      "target":10000
    }
    return render(request,'project/project.html',context)