from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
def dashboard(request):
    return render(request,'dashboard/dashboard.html')


def home(request):
    
    return render(request,'dashboard/homepage.html')

class messege(ListView):
    model = messeges
    template_name = 'dashboard/view_msg.html'
    ordering = ['-id']

class add_msg(CreateView):
    model = messeges
    form_class = msgform
    template_name = 'dashboard/add_msg.html'
    #fields = '__all__'
 

class delete_msg(DeleteView):
    model = messeges
    template_name = 'dashboard/del_msg.html'
    success_url = reverse_lazy('mess')

