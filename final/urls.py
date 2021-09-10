from django.urls import path
from django.views.generic.base import View
from . import views
from .views import *


urlpatterns = [
    path('view/', view_final.as_view(), name="view"),
    path('search_final/',views.search_final, name="search_final"),

    path('view_cr/', view_cr.as_view(), name="view_cr"),
    path('search_cr/',views.search_cr, name="search_cr"),


]