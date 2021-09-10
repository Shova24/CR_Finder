from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('dashboard/',views.dashboard, name="dashboard"),
    path('home/',views.home, name="home"),


    path('mess/', messege.as_view(), name="mess"),
    path('add_msg/', add_msg.as_view(), name="add_msg"),
    path('delete_msg/<int:pk>', delete_msg.as_view(), name="del_msg"),
   
]