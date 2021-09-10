from django.urls import path
from . import views
from .views import *


urlpatterns = [
 
    path('view_course/', view_course.as_view(), name="view_course"),
    path('search_course/',views.search_course, name="search_course"),
    path('add_course/', add_course.as_view(), name="add_course"),
    path('edit_course/<int:pk>/', edit_course.as_view(), name="edit_course"),
    path('delete_course/<int:pk>', delete_course.as_view(), name="del_course"),

]