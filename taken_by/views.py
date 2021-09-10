
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class add(CreateView):
    model = Course_taken
    form_class = Take_Form
    template_name = 'taken_by/add.html'
    success_url = reverse_lazy('view')

class view_taken(ListView):
    model = Course_taken
    template_name = 'taken_by/list.html'
    ordering = ['-id']


class edit(UpdateView):
    model = Course_taken
    form_class = Take_Form
    template_name = 'taken_by/edit.html'
    success_url = reverse_lazy('view')
    

class delete(DeleteView):
    model = Course_taken
    template_name = 'taken_by/del.html'
    success_url = reverse_lazy('view')
'''
def search_taken(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = searched.split()
        try:
            course = searched[0]
            try:
                semester = searched[1]
                a = Course_taken.objects.filter(section__batch__name__contains=batch, section__section=section)
            except:
                cr = CRR.objects.filter(section__batch__name__contains=batch)
        except:
             # 'invalid...'
            return render(request, 'CR/view_cr.html')
        return render(request,'CR/view_cr.html', {'cr':cr,'searched': searched})
    else:
        return render(request,'CR/view_cr.html')   

'''
def search_taken(request):
    if request.method == "POST":
        searched = request.POST['searched']
        print("\n\nsearch: ",searched,'\n\n')
        #searched = searched.split()
        try:
            course = searched
            print("\n\n course: ",course,"\n\n")
            cor = Course_taken.objects.filter(course__title__contains=course)
            print("\n\n cor : ",cor,"\n\n") 
        except:
             # 'invalid...'
            return render(request, 'taken_by/list.html')
        return render(request,'taken_by/list.html', {'cor':cor,'searched': searched})
       
    else:
       return render(request,'taken_by/list.html')  
    '''
    if request.method == "POST":
        searched = request.POST['searched']
        course = Course_taken.objects.filter(course__contains=searched)
        return render(request,'taken_by/list.html', {'course':course,'searched': searched})
    else:
        return render(request,'taken_by/list.html')
'''


# Create your views here.
def home(request):
    return render(request,'taken_by/main.html')