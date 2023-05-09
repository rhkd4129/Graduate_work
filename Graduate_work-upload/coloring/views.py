from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 
from django.core.files import File
from django.shortcuts import redirect, render,resolve_url,get_object_or_404

from io import BytesIO

from .forms import searchForm,uploadForm_2
from .models import Advice,SearchImage,TransImage
from .image_db_save import craw
from .image_preprocessing import dbobject_to_np,ani_to_edge,np_to_pil,real,image_sharpening







@login_required
def crawing(request):
        form  = searchForm(request.POST,request.FILES)
        if form.is_valid():
            advice = form.save(commit=False)
            advice.author = request.user
            keyword = form.cleaned_data['keywords']
            keyword,image_files = craw(keyword,6)
            advice.save()
            if keyword is None or image_files is None:
                messages.error(request,'인터넷 오류 다시 시도해 주세요')
                form = searchForm()
                return render(request,'coloring/search.html',{'form':form})
        
            i=4
            for image_data in image_files:
                advice_image = SearchImage.objects.create(advice=advice,author=request.user)
                advice_image.search_image.save(f'image{i}.jpg', File(image_data),save=False)
                advice_image.save()
                i+=1
            # return redirect(advice)
            return advice
    # else:
    #     form = searchForm()
    # return render(request,'coloring/search.html',{'form':form})

def upload_view(request):
        form_1 = searchForm(request.POST)
        form_2 = uploadForm_2(request.POST, request.FILES)
        if form_1.is_valid() and form_2.is_valid():
            advice = form_1.save(commit=False)
            advice.author = request.user
            advice.save()

            custom_image = form_2.save(commit=False)

            custom_image.author = request.user
            custom_image.advice = advice
            custom_image.save()
            return advice
            # return redirect(advice)
    # else:
    #     form_1 = searchForm()
    #     form_2 = uploadForm_2()
    # return render(request, 'coloring/upload.html', {'searchForm': searchForm, 'uploadForm_2': uploadForm_2})




def all(request):
    if request.method == 'POST':
        btn_value   = request.POST.get('btn')
        if btn_value == '1':
            return redirect(crawing(request))
        elif btn_value =='2':
            return redirect(upload_view(request))
    else:
        form_1 = searchForm()
        form_2 = uploadForm_2()

    return render(request, 'coloring/search.html', {'searchForm': searchForm, 'uploadForm_2': uploadForm_2})






@login_required
def crawing_result(request,advice_pk):
    advice = get_object_or_404(Advice,id = advice_pk)#id로써도되고pk로써도된다? ,,.?
    adviceimage = SearchImage.objects.filter(advice_id = advice_pk)
    

    if request.method == 'POST':
        button_value = request.POST.get('button_value')
        if not TransImage.objects.filter(advice_id=advice_pk,author=request.user,searchimage_id=button_value).exists():

            adviceimage = SearchImage.objects.filter(advice_id = advice_pk,id=button_value,author=request.user)[0]
            
            # 데이터베이스에서 필터 조건에 맞게 객체 불러오기 
            np_image = dbobject_to_np(adviceimage)

            #GAN을 사용해 변환하는 함수 내부적으로 함수가 포함되어잇음
            easy,hard = real(np_image)
            #변환된 모델에서 edge추출
            
            #sketch = image_sharpening(np_image)

            #numpy image에서 piilow로 변환
            pil_img_1 = np_to_pil(easy)
            pil_img_2 = np_to_pil(hard)

            bytes_io = BytesIO()
            pil_img_1.save(bytes_io, format='PNG')
            trans_image_file_1 = File(bytes_io, name='trans_image_1.png')

            bytes_io = BytesIO()
            pil_img_2.save(bytes_io, format='PNG')
            trans_image_file_2 = File(bytes_io, name='trans_image_2.png')
        

            #adviceimage.trans_image = File(trans_image_file)
            transimage_1 = File(trans_image_file_1)
            transimage_2 = File(trans_image_file_2)
            TransImage.objects.create(advice=advice,author=request.user,searchimage_id=button_value,trans_image=transimage_1)
            TransImage.objects.create(advice=advice,author=request.user,searchimage_id=button_value,trans_image=transimage_2)
    
        return redirect('coloring:trans_image_result',advice_pk= advice_pk,button_value = button_value)
    else:
       context = {'advice': advice, 'adviceimage': adviceimage}
    

    return render(request, 'coloring/result.html',context)


@login_required
def trans_image_result(request,advice_pk,button_value):
    
    #adviceimage = TransImage.objects.filter(advice_id = advice_pk,searchimage_id=button_value,author=request.user)[0]
    trans = TransImage.objects.filter(advice_id=advice_pk,author=request.user,searchimage_id=button_value)
    context = {'adviceimage':trans,'button_value':button_value,'advice_pk':advice_pk}
    return render(request,'coloring/trans_image_result.html',context)

@login_required
def user_page(request,username):
    page_user = get_object_or_404(get_user_model(),username = username)
    adivce_list = Advice.objects.filter(author = page_user)
    adivce_list_count = adivce_list.count()
    
    return render(request,'coloring/user_page.html',{
        'page_user':page_user,
        'adivce_list':adivce_list,
        'adivce_list_count':adivce_list_count,
    })


@login_required
def user_page_trans_image(request,username,keywords,name):
    page_user = get_object_or_404(get_user_model(),username = username)
    # adivce_list = Advice.objects.filter(author = page_user,advice_id=advice_pk)
    trans_image_list = Advice.objects.filter(name=name,author = page_user,keywords=keywords)
    print(len(trans_image_list))
    trans_images = trans_image_list[0].trans_search.all()

    # print( AdviceImage.objects.filter(advice__in=trans_image_list))
    return render(request,'coloring/user_page_trans_image.html',{
        'page_user':page_user,
        'trans_image_list':trans_image_list,   
        'trans_images':trans_images,
    })