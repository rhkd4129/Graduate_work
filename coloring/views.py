
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 
from django.core.files import File
from django.shortcuts import redirect, render,resolve_url,get_object_or_404

from io import BytesIO

from .forms import searchForm
from .models import Advice,AdviceImage
from .image_db_save import craw
from .image_preprocessing import dbobject_to_np,ani_to_edge,np_to_pil,real,image_sharpening






@login_required
def crawing(request):
    if request.method =='POST':
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
                advice_image = AdviceImage.objects.create(advice=advice,author=request.user)
                advice_image.image.save(f'image{i}.jpg', File(image_data),save=False)
                advice_image.save()
                i+=1
            return redirect(advice)
    else:
        form = searchForm()
    return render(request,'coloring/search.html',{'form':form})









@login_required
def crawing_result(request,advice_pk):
    advice = get_object_or_404(Advice,id = advice_pk)#id로써도되고pk로써도된다? ,,.?
    adviceimage = AdviceImage.objects.filter(advice_id = advice_pk)
    

    if request.method == 'POST':
        button_value = request.POST.get('button_value')

        adviceimage = AdviceImage.objects.filter(advice_id = advice_pk,id=button_value,author=request.user)[0]
        
        # 데이터베이스에서 필터 조건에 맞게 객체 불러오기 
        np_image = dbobject_to_np(adviceimage)

        #GAN을 사용해 변환하는 함수 내부적으로 함수가 포함되어잇음
        np_image = real(np_image)

        #변환된 모델에서 edge추출
        sketch=ani_to_edge(np_image)

        sketch = image_sharpening(sketch)

        #numpy image에서 piilow로 변환
        pil_img = np_to_pil(sketch)
        bytes_io = BytesIO()
        pil_img.save(bytes_io, format='PNG')

        trans_image_file = File(bytes_io, name='trans_image.png')
        adviceimage.trans_image = File(trans_image_file)
        adviceimage.save()
        #데이터베이스에 저장
        return redirect('coloring:trans_image_result',advice_pk= advice_pk,button_value = button_value)
    else:
       context = {'advice': advice, 'adviceimage': adviceimage}
    

    return render(request, 'coloring/result.html',context)


@login_required
def trans_image_result(request,advice_pk,button_value):
   
    adviceimage = AdviceImage.objects.get(advice_id = advice_pk,id=button_value,author=request.user)
    # file_path = adviceimage.trans_image.path
    context = {'adviceimage':adviceimage,'button_value':button_value,'advice_pk':advice_pk}
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

    # print( AdviceImage.objects.filter(advice__in=trans_image_list))
    return render(request,'coloring/user_page_trans_image.html',{
        'page_user':page_user,
        'trans_image_list':trans_image_list,   
    })


# @login_required
# def trans_image_result(request,advice_pk,button_value):
#    adviceimage = AdviceImage.objects.get(advice_id = advice_pk,id=button_value,author=request.user)
#    context = {'adviceimage':adviceimage,'button_value':button_value,'advice_pk':advice_pk}
#    return render(request,'coloring/show_trans_image_result.html',context)




 # <form method="post" action="{% url 'coloring:trans_image_result' advice_pk=advice_pk button_value=button_value %}">
 #           {% csrf_token %} 
 #           <button id="download-btn" type="submit">이미지 다운로드</button>
 #       </form>

