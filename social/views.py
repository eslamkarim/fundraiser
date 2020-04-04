from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
  return render(request, 'social/login.html')

def home(request):
  request.session['logged_in_user'] = request.user.user_id
  print(request.user.user_id)
  print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
  return redirect('home')