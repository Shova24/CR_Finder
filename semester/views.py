from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
class add_sem(CreateView,ListView):
    model = Semester
    form_class = semForm
    template_name = 'semester/list_semester.html'
    success_url = reverse_lazy('add_sem')


   
class edit_sem(UpdateView):
    model = Semester
    form_class = semForm
    template_name = 'semester/edit_semester.html'
    

class delete_sem(DeleteView):
    model = Semester
    template_name = 'semester/del_semester.html'
    success_url = reverse_lazy('add_sem')