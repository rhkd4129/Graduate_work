from django.shortcuts import redirect, render
from django.shortcuts import get_list_or_404,get_object_or_404
from ..forms import searchForm,PostForm
from django.db.models import Q
from django.views.generic import ListView,DetailView,FormView,CreateView
from django.views.generic import UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Post,Comment
from django.contrib.auth import get_user_model


def UserPage(request,username):

    page_user = get_object_or_404(get_user_model(),username = username)
    post_list = Post.objects.filter(author = page_user)
    return render(request,"blog/user_page.html",{'page_user':page_user,'post_list':post_list})





def BlogList(request):
    posts = Post.objects.all()
    q = request.GET.get('search','')
    if q:
        posts = Post.objects.filter(Q(title__icontains = q)|Q(content__icontains =q)).distinct()
    return render(request,'blog/blog_list.html',{'posts':posts,'q':q,})#'form':searchForm,



def blog_detail(request,post_pk):
    post = get_object_or_404(Post,id = post_pk)#id로써도되고pk로써도된다? ,,.?
    comments = Comment.objects.filter(post_id = post_pk)
    return render(request,'blog/blog_detail.html',{'post':post,'comments':comments})

# class BlogDeatil(DetailView,ListView):
#      login_url = settings.LOGIN_URL
#      model = Post

#      template_name ='blog/blog_detail.html'
#      context_object_name = 'post'
#      pk_url_kwarg = "post_pk"
# blog_detail = BlogDeatil.as_view()


class BlogCreate(LoginRequiredMixin,CreateView):
   # login_url = #reverse_lazy('blog:post_list')#settings.LOGIN_URL
    model =Post
    form_class = PostForm
    template_name = 'blog/form.html'
    pk_url_kwarg = "post_pk"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)
blog_create = BlogCreate.as_view()


@login_required
def blog_edit(request,post_pk):
    post = get_object_or_404(Post,pk =post_pk)

    if post.author != request.user:
        messages.error(request,'작성자만 수정가능') #이부분은 데코레이터로 할것
        return redirect(post)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post) 
    else:
        form = PostForm(instance=post)
    return render(request,'blog/form.html',{'form':form,})



def blog_delete(request,post_pk):
    post = get_object_or_404(Post,pk =post_pk)
    if post.author != request.user:
        messages.error(request,'작성자만 삭제가능') #이부분은 데코레이터로 할것
        return redirect(post)
    if request.method =='POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request,'blog/blog_delete.html',{'post':post})
  

