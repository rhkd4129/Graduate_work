from django.shortcuts import render
from .melonchart import my_dict
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import searchForm
from .image_crawing import image_c
# Create your views here.

def melon_chart(request):
   
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict,})




def search_image(request):

    if request.method =='POST':
        form  = searchForm(request.POST)
        if form.is_valid():
            #search = form.cleaned_data['search']
            a = image_c(form.cleaned_data['search'])
            context = {'form':form, 'search':form.cleaned_data['search'],'a':a}

            
            return render(request,'crawling/search_image.html',context)
    else:
        form = searchForm()

    
    return render(request,'crawling/search_image.html',{'form':form})