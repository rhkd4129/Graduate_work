from django.shortcuts import redirect, render
from .melonchart import my_dict
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import searchForm
from .image_crawing import craw
from django.views.generic import CreateView,FormView
from .models import Advice
from .forms import searchForm
from django.shortcuts import get_object_or_404
from .image import instance_1,instance_2
# from copy import copy
#from .image_preprocessing import cvt_image_save
instance = [instance_1,instance_2]
def melon_chart(request):
   
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict})


# class AdviceCrate(CreateView):
#     model =Advice
#     form_class = searchForm
#     template_name='crawling/search_image.html'

#     def form_valid(self, form):
        
#         return super().form_valid(form)

def upload(request):
    if request.method == "POST":
        for image in images:
            MultipleImage.objects.create(images=image)
    images = MultipleImage.objects.all()
    return render(request, 'index.html', {'images': images})


def search_image(request):
    #advice = get_object_or_404(Advice)
    if request.method =='POST':
        form  = searchForm(request.POST,request.FILES)

        if form.is_valid():
            #keyward = form.cleaned_data['keyword']
            #find_image_number  = form.cleaned_data['find_image_number']
            cleaned_data_copy = form.cleaned_data.copy()
            form.cleaned_data['searh_result_image'] = instance
            cleaned_data_copy['keyword'] = 'keyword'
            print(form.cleaned_data)
            print(cleaned_data_copy)



            #keyward,cvt_images,image_length = craw(keyward,find_image_number)
            #advice = form.save(commit=False)
            cvt_images =request.FILES.getlist('searh_result_image')
            print(cvt_images)
            for image in cvt_images:
                Advice.objects.create(searh_result_image=image)
            # images = advice.obejcts.all()
            # for image in cvt_images:
            #     advice.searh_result_image = image
            #advice.searh_result_image = instance
            advice = form.save()
            print(cleaned_data_copy['keyword'])
           
            #advice.objects.create() = cvt_images
    
            # context = { 
            #             'advice':advice,
            #             'form':form,
            #             'keyward':keyward,
            #             'find_image_count':find_image_number,
            #             'cvt_images':images
            #             }
            
            
            return render(request,'crawling/search_image.html',{'advice':advice})
            #return redirect(advice)
           
            #return render(request,'crawling/search_image.html',context)
            #return render(request,'crawling/search_image.html',{'keyward':keyward})
    else:
        form = searchForm()
    #
    return render(request,'crawling/search_image.html',{'form':form})




# def search_image(request):

#     if request.method =='POST':
#         form  = searchForm(request.POST)
#         if form.is_valid():
#             keyward = form.cleaned_data['search']
#             find_image_count  = form.cleaned_data['image_number']
#             keyward,cvt_images,image_length = craw(keyward,find_image_count)
#             context = {'form':form,
#                         'keyward':keyward,
#                         'find_image_count':find_image_count,
#                         'cvt_images':cvt_images
#                         }

            
#             return render(request,'crawling/search_image.html',context)
#     else:
#         form = searchForm()

    
#     return render(request,'crawling/search_image.html',{'form':form})