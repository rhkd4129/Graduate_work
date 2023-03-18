from django import forms
from .models import Post,Comment


class searchForm(forms.Form):
    search = forms.CharField(label='Search')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','photo','is_public','gender']#'__all__'
        #fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        labels = {'message': '댓글내용',}
        widgets={
            "message": forms.Textarea(attrs= 
            {'class': 'form-control',
            'placeholder': "This is a write message 200",
            'rows': 7,}),
        }
     

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
        # self.fields['message'].widget.attrs = {
        #     'class': 'form-control',
        #     'placeholder': "This is a write message 200",
        #     'rows': 7
        # }
