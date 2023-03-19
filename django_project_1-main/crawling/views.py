from django.shortcuts import render
from .melonchart import my_dict
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import searchForm
from .image_crawing import craw
#from .image_preprocessing import cvt_image_save

def melon_chart(request):
   
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict,})




def search_image(request):

    if request.method =='POST':
        form  = searchForm(request.POST)
        if form.is_valid():
            keyward = form.cleaned_data['search']
            find_image_count  = form.cleaned_data['image_number']
            keyward,cvt_images,image_length = craw(keyward,find_image_count)
            context = {'form':form,
                        'keyward':keyward,
                        'find_image_count':find_image_count,
                        'cvt_images':cvt_images
                        }

            
            return render(request,'crawling/search_image.html',context)
    else:
        form = searchForm()

    
    return render(request,'crawling/search_image.html',{'form':form})