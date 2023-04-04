
from django.shortcuts import redirect, render
from .forms import searchForm
from .models import Advice,AdviceImage
from .image_db_save import craw
from django.shortcuts import get_object_or_404
from django.core.files import File

from io import BytesIO
# Image.open(fp)
def qwer(request):
    if request.method =='POST':
        form  = searchForm(request.POST,request.FILES)
        if form.is_valid():
            advice = form.save(commit=False)
            keyword = form.cleaned_data['keywords']
            keyword,image_files = craw(keyword, 2)
            advice.save()
            i=4
            for image_data in image_files:
                advice_image = AdviceImage.objects.create(advice=advice)
                advice_image.image.save(f'image{i}.jpg', File(image_data),save=False)
                advice_image.save()
                i+=1
            
            return redirect(advice)
    else:
        form = searchForm()
    return render(request,'qwer/search.html',{'form':form})

def result(request,advice_pk):
    advice = get_object_or_404(Advice,id = advice_pk)#id로써도되고pk로써도된다? ,,.?
    adviceimage = AdviceImage.objects.filter(advice_id = advice_pk)
    print(adviceimage)
    print(advice)
    context = {'advice': advice, 'adviceimage': adviceimage}
    return render(request, 'qwer/result.html',context)



# def search_image(request):
#     if request.method =='POST':
#         form  = searchForm(request.POST,request.FILES)
#         if form.is_valid():
#             advice = form.save(commit=False)
#             keyword = form.cleaned_data['keyword']
#             find_image_number = form.cleaned_data['find_image_number']
#             keyword,path_list,file_name_list= craw(keyword,find_image_number)
#             adivces=[]
#             # for i in range(find_image_number):
#                 # with open(path_list[i]+file_name_list[i], 'rb') as f:
#                     # advice.searh_result_image.save(file_name_list[i], File(f), save=False)                                                                      
#                 # adivces[i] = Advice.objects.create(customer='a',keyword=keyword,find_image_number=i,searh_result_image=File(f))                    
#             adivces1= Advice.objects.create(customer='a',keyword=keyword,find_image_number=1,searh_result_image=path_list[0]+file_name_list[0])   
#             adivces2= Advice.objects.create(customer='a',keyword=keyword,find_image_number=2,searh_result_image=path_list[1]+file_name_list[1])                                     
#             advice_list = Advice.objects.all()

            
#             return render(request,'crawling/search_image.html',{'advice_list':advice_list})          
#     else:
#         form = searchForm()
#     return render(request,'crawling/search_image.html',{'form':form})
