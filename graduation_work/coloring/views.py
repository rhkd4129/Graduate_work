
from django.shortcuts import redirect, render,resolve_url
from .forms import searchForm
from .models import Advice,AdviceImage
from .image_db_save import craw
from django.shortcuts import get_object_or_404
from django.core.files import File
from .image_preprocessing import dbobject_to_np,ani_to_edge,np_to_pil
from io import BytesIO
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 


# {% for field in form %}
# <div class="form-group">
#    <labl for=""></labl>
#    <input type="" class="form-control" id="" placeholder="" name="">
# </div>
# {% endfor %}


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
        np_image = dbobject_to_np(adviceimage)
        sketch=ani_to_edge(np_image)
        pil_img = np_to_pil(sketch)

        bytes_io = BytesIO()
        pil_img.save(bytes_io, format='PNG')

        trans_image_file = File(bytes_io, name='trans_image.png')
        adviceimage.trans_image = File(trans_image_file)
        adviceimage.save()

        return redirect('coloring:trans_image_result',advice_pk= advice_pk,button_value = button_value)
    else:
       context = {'advice': advice, 'adviceimage': adviceimage}
    

    return render(request, 'coloring/result.html',context)


@login_required
def trans_image_result(request,advice_pk,button_value):
    # advice = get_object_or_404(Advice,id = advice_pk)#id로써도되고pk로써도된다? ,,.?
    adviceimage = AdviceImage.objects.get(advice_id = advice_pk,id=button_value,author=request.user)
    context = {'adviceimage':adviceimage,'button_value':button_value}
    
    return render(request,'coloring/trans_image_result.html',context)

def show_trans_image_result(request,advice_pk,button_value):
    context = {'button_value':button_value}
    return render(request,'coloring/show_trans_image_result.html',context)


#  <table class="table table-bordered table-hover mt-5">
#       <tbody>
#         {% if button_value %}
#         <tr>
#           <td>Button value is {{ button_value }}</p></td>
#         </tr>
#         {% endif %}

#         {% if adviceimage %}
#         {{adviceimage|length}}
#           {% for image in adviceimage %}
#           <td>
            
#             <img src="{{image.image.url}}"  alt="a"/>  

#             <form method="post">
#             {% csrf_token %}
#               <button type="submit" name="button_value" value={{image.id}}>{{image.id}}</button>
#             </form> 
#           </td>
#           {% endfor %}
#     </tbody>
#   </table>        
