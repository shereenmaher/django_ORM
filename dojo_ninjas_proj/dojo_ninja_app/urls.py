from django.urls import path
from . import views

urlpatterns = [

    path('', views.view_dojo),
    path('create_dojo', views.create_dojo),
    path('viewdojo', views.view_dojo),
    path('createninja', views.create_ninja),
    path('viewninja', views.view_ninja),
    path('delete_dojo/<int:dojo_id>', views.delete_dojo),

]