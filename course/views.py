from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class add_course(CreateView):
    model = Course
    form_class = courseForm
    template_name = 'course/add_course.html'
    success_url = reverse_lazy('view_course')

class view_course(ListView):
    model = Course
    template_name = 'course/list_course.html'
    ordering = ['-id']

def search_course(request):

    if request.method == "POST":
        searched = request.POST['searched']
        course = Course.objects.filter(title__contains=searched)

        return render(request,'course/list_course.html', {'course':course,'searched': searched})
    else:
        return render(request,'course/list_course.html')
    
class edit_course(UpdateView):
    model = Course
    form_class = courseForm
    template_name = 'course/edit_course.html'
    

class delete_course(DeleteView):
    model = Course
    template_name = 'course/del_course.html'
    success_url = reverse_lazy('view_course')