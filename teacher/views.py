from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class add_teacher(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/add_teacher.html'
    success_url = reverse_lazy('view_teacher')

class view_teacher(ListView):
    model = Teacher
    template_name = 'teacher/view_teacher.html'
    ordering = ['-id']

def search(request):
    print('\n\n method= '+request.method,'\n\n')

    if request.method == "POST":
        searched = request.POST['searched']
        teacher = Teacher.objects.filter(T_name__contains=searched)
        print("\n: ",teacher)
        teacher_p = Teacher.objects.all()
        print("\n: ",teacher_p)

        return render(request,'teacher/view_teacher.html', {'teacher':teacher,'searched': searched,"teacher_p":teacher_p})
    else:
        return render(request,'teacher/view_teacher.html')
    
class edit_teacher(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/edit_teacher.html'
    

class delete_teacher(DeleteView):
    model = Teacher
    template_name = 'teacher/del_teacher.html'
    success_url = reverse_lazy('view_teacher')