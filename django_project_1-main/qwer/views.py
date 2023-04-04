
from django.shortcuts import redirect, render,resolve_url
from .forms import searchForm
from .models import Advice,AdviceImage
from .image_db_save import craw
from django.shortcuts import get_object_or_404
from django.core.files import File


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
    

    if request.method == 'POST':
        button_value = request.POST.get('button_value')
        # if button_value == '1':
        #     value = 1
        # elif button_value == '2':
        #     value = 2
        return redirect('qwer:trans_image_result',advice_pk= advice_pk,button_value = button_value)
    else:
       context = {'advice': advice, 'adviceimage': adviceimage}
    

    return render(request, 'qwer/result.html',context)


def trans_image_result(request,advice_pk,button_value):
    advice = get_object_or_404(Advice,id = advice_pk)#id로써도되고pk로써도된다? ,,.?
    adviceimage = AdviceImage.objects.filter(advice_id = advice_pk)
    context = {'button_value':button_value}

    return render(request,'qwer/trans_image_result.html',context)

