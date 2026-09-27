from django.db import models


class User(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    age=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def get_users():
    users=User.objects.all()
    return users

def create_newuser(data):
    firstname=data['firstname']
    lastname=data['lastname']
    email=data['email']
    age=data['age']
    User.objects.create(firstname=firstname,lastname=lastname,email=email,age=age)

