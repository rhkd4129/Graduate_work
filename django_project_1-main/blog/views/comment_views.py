from ..models import Post,Comment
from ..forms import CommentForm
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def comment_create(request,post_pk):
    post = get_object_or_404(Post,pk = post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            # print(comment)  #message가담겨잇다
            # print(post)#post의 title이 담겨잇는데 id도 담겨있다(모든 정보??)
            comment.save()
            return redirect(post) 
    else:
        form = CommentForm()
    return render(request,'comment/comment_create.html',{"form":form})



@login_required
def comment_edit(request,comment_pk):
    comment = get_object_or_404(Comment,pk = comment_pk)
    if comment.author != request.user:
         messages.error(request,'작성자만 수정가능')
         return redirect(comment.post)
    if request.method == 'POST':
        form =CommentForm(request.POST,instance=comment)
        if form.is_valid():
            comment = form.save()
            messages.success(request,'포스티저장')
            return redirect(comment.post)
    else:
        form = CommentForm(instance = comment)

    return render(request,'comment/comment_create.html',{'form':form,'comment':comment})




@login_required
def comment_delete(request,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if comment.author != request.user:
         messages.error(request,'작성자만 수정가능')
         return redirect(comment.post)

    if request.method == 'POST':
        comment.delete()
        messages.success(request,'포스팅삭제')
        return redirect(comment.post)
    return render(request,'comment/comment_delete.html',{'comment':comment,})


