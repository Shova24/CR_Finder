from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('view_teacher/', view_teacher.as_view(), name="view_teacher"),
    path('search/',views.search, name="search"),
    path('add_teacher/', add_teacher.as_view(), name="add_teacher"),
    path('edit_teacher/<int:pk>/', edit_teacher.as_view(), name="edit_teacher"),
    path('delete_teacher/<int:pk>', delete_teacher.as_view(), name="del_teacher"),


]