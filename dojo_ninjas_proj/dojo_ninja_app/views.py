from django.shortcuts import render,HttpResponse,redirect
from . import models


def create_dojo(request):
    if request.method== 'POST':
        models.create_newdojo(request.POST)
        return redirect("/")
    else:
        context = {
            "dojos": models.get_dojos()
        }
    return render(request, "dojo_ninja.html", context)

def view_dojo(request):
    context = {
        "dojos": models.get_dojos()
    }
    return render(request, "dojo_ninja.html", context)

def create_ninja(request):
    if request.method== 'POST':
        models.create_newninja(request.POST)
        return redirect("/")
    else:
        context = {
                "dojos": models.get_dojos()
        }
    return render(request, "dojo_ninja.html", context)

def view_ninja(request):
    context = {
        "ninjas": models.get_ninjas()
    }
    return render(request, "dojo_ninja.html", context)

def delete_dojo(request, dojo_id):
    dojo = models.Dojo.objects.get(id=dojo_id)
    dojo.delete()

    return redirect("/")