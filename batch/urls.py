from django.urls import path
from . import views
from .views import *


urlpatterns = [
 
    path('add_batch/', add_batch.as_view(), name="add_batch"),
    path('edit_batch/<int:pk>/', edit_batch.as_view(), name="edit_batch"),
    path('delete_batch/<int:pk>', delete_batch.as_view(), name="del_batch"),

    path('add_sec/', add_sec.as_view(), name="add_sec"),
    path('edit_sec/<int:pk>/', edit_sec.as_view(), name="edit_sec"),
    path('delete_sec/<int:pk>', delete_sec.as_view(), name="del_sec"),
]