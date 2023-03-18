
# @login_required()
# def blog_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save()
#             return redirect(post)
#     else:
#         form = PostForm()
#     return render(request,'blog/form.html',{'form':form,})



# class BlogEdit(LoginRequiredMixin,UpdateView):
#     model = Post
#     form_class = PostForm
#     pk_url_kwarg = "post_pk"
#     template_name ='blog/form.html'
   
#     def form_valid(self, form):
#         if self.object.author != self.request.user:   #request.user 현재 로그인 user instance
#             messages.error(self.request,'작성자만 수정가능')
#             redirect()
#         return super().form_valid(form)
# blog_edit = BlogEdit.as_view()



# class BlogDelete(DeleteView):
#     pk_url_kwarg = "post_pk"
#     template_name ='blog/blog_delete.html'
#     model=Post
#     success_url = reverse_lazy('blog:post_list')
# blog_delete = BlogDelete.as_view()


