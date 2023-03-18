
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User

class SignupForm(UserCreationForm):
    def __init__(self, *args ,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required= True
        self.fields['phone_number'].required= True


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','email','phone_number'] 

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email = email)
            if qs.exists():
                raise forms.ValidationError("이미등록된이메일")
            return email


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','phone_number']









