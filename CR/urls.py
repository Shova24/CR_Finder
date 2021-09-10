from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('view_cr/', view_cr.as_view(), name="view_cr"),
    path('search_cr/',views.search_cr, name="search_cr"),
    path('add_cr/', add_cr.as_view(), name="add_cr"),
    path('edit_cr/<int:pk>/', edit_cr.as_view(), name="edit_cr"),
    path('delete_cr/<int:pk>', delete_cr.as_view(), name="del_cr"),

    
  path('show_cr/', views.show_cr, name="show_cr"),

]