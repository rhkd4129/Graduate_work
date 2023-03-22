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
from copy import deepcopy
#from .image_preprocessing import cvt_image_save
# from .image import instance_1
def melon_chart(request):
   
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict})


# from django import forms
# from django.core.exceptions import ValidationError

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(widget=forms.Textarea)

#     def clean(self):
#         cleaned_data = super().clean()
#         email = cleaned_data.get('email')
#         message = cleaned_data.get('message')

#         if email and not email.endswith('@example.com'):
#             raise ValidationError("Only example.com emails are allowed.")

#         if message:
#             num_words = len(message.split())
#             if num_words < 4:
#                 raise ValidationError("Enter a message with at least 4 words.")

# def upload(request):
#     if request.method == "POST":
#         for image in images:
#             MultipleImage.objects.create(images=image)
#     images = MultipleImage.objects.all()
#     return render(request, 'index.html', {'images': images})
    # def save_model(self, request, obj, form, change):
    #     searh_result_image = request.FILES.getlist('searh_result_image')
    #     for f in searh_result_image:
    #         instance = Advice(searh_result_image=f)
    #         instance.save()

def search_image(request):
    if request.method =='POST':
        form  = searchForm(request.POST,request.FILES)
        if form.is_valid():
            keyward = form.cleaned_data['keyword']
            find_image_number  = form.cleaned_data['find_image_number']
            #searh_result_image =  form.cleaned_data['searh_result_image']
            searh_result_image = request.FILES.getlist('searh_result_image')
            #keyward,cvt_images,image_length = craw(keyward,find_image_number)
            advice = form.save(commit=False)
  
            
            #advice.gender = 'M'
            # advice.obejcts.all()
            

            
            for image in searh_result_image:
                #Advice.objects.create(searh_result_image=image)
                instance = advice(keyword=keyward,find_image_number= find_image_number,searh_result_image=searh_result_image)
                instance.save()
            #images = advice.obejcts.all()
            advice.save()
            print(form.cleaned_data)
            #advice.objects.create() = cvt_images
            #form.cleaned_data['searh_result_image'] = cvt_images
         
            # context = { 
            #             'advice':advice,
            #             'form':form,
            #             'keyward':keyward,
            #             'find_image_count':find_image_number
            #           #  'cvt_images':images
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