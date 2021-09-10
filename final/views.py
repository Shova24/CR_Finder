
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from taken_by.models import *
from taken_by.forms import *
from CR.models import *
from CR.forms import *

from django.urls import reverse_lazy

# Create your views here.


class view_final(ListView):
    model = Course_taken
    template_name = 'final/search.html'
    ordering = ['-id']



def search_final(request):
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
            return render(request, 'final/search.html')
        return render(request,'final/search.html', {'cor':cor,'searched': searched})
       
    else:
       return render(request,'final/search.html')  



class view_cr(ListView):
    model = CRR
    template_name = 'final/search_cr.html'
    ordering = ['-id']

def search_cr(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = searched.split()
        try:
            batch = searched[0]
            print('batch : ', batch,'\n\n')
            try:
                section = searched[1]
                cr = CRR.objects.filter(section__batch__name__contains=batch, section__section=section)
                #secttion er batch er name
                print('section : ', section, ' - cr : ', cr, '\n\n')
            except:
                cr = CRR.objects.filter(section__batch__name__contains=batch)
                print('section except: ', section, ' - cr : ', cr, '\n\n')
        except:
             # 'invalid...'
            return render(request,  'final/search_cr.html')
        return render(request, 'final/search_cr.html', {'cr':cr,'searched': searched})
    else:
        return render(request, 'final/search_cr.html')   


