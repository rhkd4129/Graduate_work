from django.shortcuts import render
from .melonchart import my_dict
from django.views.generic import ListView
from django.core.paginator import Paginator
# Create your views here.

def melon_chart(request):
   
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict,})