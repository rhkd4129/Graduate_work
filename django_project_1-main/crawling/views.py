from django.shortcuts import render
from .melonchart import my_dict
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import searchForm
# Create your views here.

def melon_chart(request):
   
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict,})

def search_image(request):

    if request.method =='POST':
        form  = searchForm(request.POST)
        print(form)
    else:
        form = searchForm()

    
    return render(request,'crawling/search_image.html',{'form':form})