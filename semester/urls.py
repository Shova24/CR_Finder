from django.urls import path
from . import views
from .views import *


urlpatterns = [
 
   
    path('add_sem/', add_sem.as_view(), name="add_sem"),
    path('edit_sem/<int:pk>/', edit_sem.as_view(), name="edit_sem"),
    path('delete_sem/<int:pk>', delete_sem.as_view(), name="del_sem"),

]