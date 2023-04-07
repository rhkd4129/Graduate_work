from django.views.generic import TemplateView


class TView(TemplateView):
    template_name = 'home.html'

# def crawing(request):
#     if request.method =='POST':
#         form  = searchForm(request.POST)
#         if form.is_valid():
#             return redirect(advice)
#     else:
#         form = searchForm()
#     return render(request,'coloring/search.html',{'form':form})
