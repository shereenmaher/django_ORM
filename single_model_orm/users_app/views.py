from django.shortcuts import render,redirect,HttpResponse
from . import models

# Create your views here.
def createuser(request):
    if request.method == 'POST':
        models.create_newuser(request.POST)
        return redirect('/viewuser')
    else:
        context = {
            "users": models.get_users()
        }
        return render(request, "users.html", context)
      
    
def viewuser(request):
    context={
        "users":models.get_users()
    }
    return render(request,"users.html",context)
    