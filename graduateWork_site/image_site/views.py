from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse,HttpRequest
from django.views.generic import ListView,DetailView
from django.views.generic import ListView,DetailView
#from django.contrib.auth import get_user_model
#from models import Post


# post_list = ListView.as_view(model=Post)

# def post_detail(request:HttpRequest,post_id:int)->HttpResponse:
#     post=get_object_or_404(Post,pk = post_id)
#     return render(request,'image_site/post_detail.html',{'post':post},)




# class PostDetailView(DetailView):
#     model = Post
#     #pk_url_kwarg='id' pk를썻다면 무방안써도됨