from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User



# Create your views here.
def index(request):
    pass
def delete(request,username):
    try:
        u = User.objects.get(username = username)
        u.delete()
        messages.sucess(request, "The user is deleted")
    except:
      messages.error(request, "The user not found")    
    return render(request, 'home.html')

