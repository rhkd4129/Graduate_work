from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SignupForm,ProfileEditForm

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required 


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = SignupForm()
    return render(request,'accounts/signup.html',{'form':form,})
# Create your views here.

@login_required
def profile_edit(request):
    
    if request.method =='POST':
        form = ProfileEditForm(request.POST,request.FILES,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    else:
        form = ProfileEditForm(instance = request.user)
    return render(request,'accounts/profile_edit.html',{'form':form})

@login_required
def password_change(request):  
    if request.method =='POST':
        form =  PasswordChangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')
    else:
        form = PasswordChangeForm(instance = request.user)
    return render(request,'accounts/password_change.html',{'form':form})
    pass


# password_change = PasswordChangeView.as_view()
