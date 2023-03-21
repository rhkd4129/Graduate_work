from django import forms
from .models import Advice


class searchForm(forms.ModelForm):
    #search = forms.CharField(label='Search')
    #image_number = forms.IntegerField( min_value=1, max_value=10,label='number')
    class Meta:
        model = Advice
        fields = ['customer','keyword','find_image_number','searh_result_image']

        widgets={
            'searh_result_image':forms.ClearableFileInput(attrs={'multiple':True})
        }