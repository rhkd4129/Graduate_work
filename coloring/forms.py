from django import forms
from .models import Advice,SearchImage




class searchForm(forms.ModelForm):
    #search = forms.CharField(label='Search')
    #image_number = forms.IntegerField( min_value=1, max_value=10,label='number')
    class Meta:
        model = Advice
        fields = ['name','keywords','age']

        # widgets={
        #     'searh_result_image':forms.ClearableFileInput(attrs={'multiple':True})
        # }




class uploadForm_2(forms.ModelForm):
    class Meta:
        model = SearchImage
        fields = ['search_image']

    