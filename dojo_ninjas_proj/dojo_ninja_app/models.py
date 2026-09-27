from django.db import models

# Create your models here.
class Dojo(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    desc=models.CharField(max_length=200,default="old dojo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    dojo=models.ForeignKey(  Dojo , related_name="ninjas",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def get_dojos():
    dojos=Dojo.objects.all()
    return dojos

def create_newdojo(data):
    name=data['name']
    city=data['city']
    state=data['state']
    desc=data['desc']
    Dojo.objects.create(name=name,city=city,state=state,desc=desc)

def get_ninjas():
    ninjas=Ninja.objects.all()
    return ninjas

def create_newninja(data):
    firstname = data['firstname']
    lastname = data['lastname']
    dojo_id = data['dojo']

    dojo = Dojo.objects.get(id=dojo_id)

    Ninja.objects.create(firstname=firstname,lastname=lastname,dojo=dojo)

