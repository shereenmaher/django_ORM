from django.urls import path
from . import views

urlpatterns = [
    path('', views.createuser),
    path('viewuser',views.viewuser),
]
