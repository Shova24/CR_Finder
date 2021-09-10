from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class add_cr(CreateView):
    model = CRR
    form_class = CR_Form
    template_name = 'CR/add_cr.html'
    success_url = reverse_lazy('view_cr')

class view_cr(ListView):
    model = CRR
    template_name = 'CR/view_cr.html'
    ordering = ['-id']
'''
def search_cr(request):
    if request.method == "POST":
        searched = request.POST['searched']
        cr = CRR.objects.filter(name__contains=searched)
        return render(request,'CR/view_cr.html', {'cr':cr,'searched': searched})
    else:
        return render(request,'CR/view_cr.html')
 
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
                print('section : ', section, ' - cr : ', cr, '\n\n')
            except:
                cr = CRR.objects.filter(section__batch__name__contains=batch)
                print('section except: ', section, ' - cr : ', cr, '\n\n')
        except:
             # 'invalid...'
            return render(request, 'CR/view_cr.html')
        return render(request,'CR/view_cr.html', {'cr':cr,'searched': searched})
    else:
        return render(request,'CR/view_cr.html')   
'''
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
            return render(request, 'CR/view_cr.html')
        return render(request,'CR/view_cr.html', {'cr':cr,'searched': searched})
    else:
        return render(request,'CR/view_cr.html')   



class edit_cr(UpdateView):
    model = CRR
    form_class = CR_Form
    template_name = 'CR/edit_cr.html'
    success_url = reverse_lazy('view_cr')
    

class delete_cr(DeleteView):
    model = CRR
    template_name = 'CR/del_cr.html'
    success_url = reverse_lazy('view_cr')

def show_cr(request):
    return render(request, 'CR/show_cr.html')