from django.urls import path
from .import views
from .views import *
urlpatterns = [

    path('register/', Register.as_view(), name='register'),
    #path('login/', login.as_view(), name='login'),


]
