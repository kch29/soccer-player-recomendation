from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from .forms import ForwardForm, MidfielderForm, DefenderForm    
from django.views.generic import TemplateView
# Create your views here.
def index(request):
    return render(request, 'index.html')

def back_setting(request):
    
    # POST REQUSET --> CONFIRM THE FORM CONTENTS --> BACK TO HOMEPAGE
    # ELSE, RENDER FORM
    if request.method == 'POST':
        form = ForwardForm(request.POST)
        form2 = MidfielderForm(request.POST)
        form3 = DefenderForm(request.POST)
        
        if form.is_valid():
            print(form.cleaned_data)
            
        if form2.is_valid():
            print(form2.cleaned_data)
            
        if form3.is_valid():
            print(form3.cleaned_data)
            
    else:
        form = ForwardForm()
        form2 = MidfielderForm()
        form3 = DefenderForm()


    return render(request, 'background_setting/back_setting.html', {'form':form, 'form2':form2, 'form3':form3})
        

def best11(request):
    candidates = models.offensive.objects.all()
    context = {'candidates':candidates}
    return render(request, 'background_setting/best11.html', context=context)

def ranking(request):
    candidates = models.defensive.objects.all()
    context = {'candidates':candidates}
    return render(request, 'background_setting/ranking.html', context=context)

def international(request):
    candidates = models.defensive.objects.all()
    context={'candidates':candidates}
    return render(request, 'background_setting/international.html', context=context)

# def option(request):
#     if request.POST:
#         number = int(request.POST['goals'])
#         models.option.objects.create(list=number)
#         return redirect(reverse('templates:index'))
#     return render(request,index.html)
#  계획 : offensive/defensive/passing -> 3개의 카테고리에서 체크박스 번호를 넘겨받아서 번호별로 가중치 부여해서 rating 책정