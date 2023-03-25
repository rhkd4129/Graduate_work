from django import forms
from .models import Advice


class searchForm(forms.ModelForm):
    #search = forms.CharField(label='Search')
    #image_number = forms.IntegerField( min_value=1, max_value=10,label='number')
    class Meta:
        model = Advice
        fields = ['customer','keyword','find_image_number']

        # widgets={
        #     'searh_result_image':forms.ClearableFileInput(attrs={'multiple':True})
        # }


    # def clean(self,value):
    #         cleaned_data = super().clean()
    #         cleaned_data['gender'] = value
    #         return cleaned_data

    # def clean_customer(self):
    #     # customer = self.cleaned_data.get('customer')
    #     self.cleaned_data['customer'] = 'fixed'
    #     return self.cleaned_data
        

    #def clean_keyword
#   #클래스 파스칼형태  claendData
    #함수느 _형태