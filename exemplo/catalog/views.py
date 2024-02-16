from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
  return render(request, 'users/home.html')

def users(request):
  user = User()
  user.name = request.POST.get('name')
  user.age = request.POST.get('age')
  user.save()  
  
  users = {
    'users': User.objects.all()
  }
  
  return render(request, 'users/users.html', users)