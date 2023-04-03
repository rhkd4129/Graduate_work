from django.shortcuts import redirect, render
from .melonchart import my_dict
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import searchForm
from .image_crawing import craw
from django.views.generic import CreateView,FormView
from .models import Advice
from .forms import searchForm
from PIL import Image
from django.shortcuts import get_object_or_404
from copy import deepcopy
#from .image_preprocessing import cvt_image_save
# from .image import pillow_image

# from django.core.files import images
pillow_image =Image.open('C:\study\graduate\django_project_1-main\duck_img_download\duck1.jpg')


def melon_chart(request):
   
    return render(request,'crawling/melon_chart.html',{'melon_chart':my_dict})

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
#django inmemoryuploadedfile
# from django.core.files.base import ContentFile, File
from django.core.files import File
from django.db.models.fields.files import FileField
from django.core.files.base import ContentFile
  #keyward,cvt_images,image_length = craw(keyward,find_image_number)
  
def search_image(request):
    if request.method =='POST':
        form  = searchForm(request.POST,request.FILES)
        if form.is_valid():
            advice = form.save(commit=False)
            keyword = form.cleaned_data['keyword']
            find_image_number = form.cleaned_data['find_image_number']
            #my_file = File(pillow_image)
            # kweyword,cvt_images,image_length = craw(keyword,find_image_number)
            
            with open('C:\Python_1821028\django_project_1-main\duck_img_download\duck1.jpg', 'rb') as f:
                advice.searh_result_image.save('filename.jpg', File(f), save=False)
                advice.save()
            return render(request,'crawling/search_image.html',{'advice':advice})          
    else:
        form = searchForm()
    return render(request,'crawling/search_image.html',{'form':form})


            #########################################################   ##################################
            #with open('C:study\graduate\django_project_1-main\duck_img_download\duck1.jpg','rb') as f:
            # advice = Advice.objects.create(
            #         customer = customer,
            #         keyword= keyword,
            #         find_image_number=find_image_number,
            #         searh_result_image =File(pillow_image))
            ##############################################################################################
            ##############################################################################################
            # 
            # advice.searh_result_image  = File(pillow_image)
            # advice.save()
            ###################################################
    
            #images = advice.obejcts.all()         
            #return render(request,'crawling/search_image.html',{'keyward':keyward})




