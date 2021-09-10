from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy


# Create your views here.
class add_batch(CreateView,ListView):
    model = Batch
    form_class = BatchForm
    template_name = 'batch/add_view_batch.html'
    success_url = reverse_lazy('add_batch')

class edit_batch(UpdateView):
    model = Batch
    form_class = BatchForm
    template_name = 'batch/edit_batch.html'
    

class delete_batch(DeleteView):
    model = Batch
    template_name = 'batch/del_batch.html'
    success_url = reverse_lazy('add_batch')


class add_sec(CreateView,ListView):
    model = Section_add
    form_class = SecForm
    template_name = 'batch/add_sec.html'
    success_url = reverse_lazy('add_sec')


class edit_sec(UpdateView):
    model = Section_add
    form_class = SecForm
    template_name = 'batch/edit_sec.html'
    

class delete_sec(DeleteView):
    model = Section_add
    template_name = 'batch/del_sec.html'
    success_url = reverse_lazy('add_sec')
