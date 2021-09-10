from django.urls import path
from django.views.generic.base import View
from . import views
from .views import *


urlpatterns = [
    path('view/', view_taken.as_view(), name="view"),
    path('search_taken/',views.search_taken, name="search_taken"),
    path('add/', add.as_view(), name="add"),
    path('edit/<int:pk>/', edit.as_view(), name="edit"),
    path('delete/<int:pk>', delete.as_view(), name="del"),
]