from django import forms
from .models import Advice,SearchImage



class searchForm(forms.ModelForm):
    class Meta:
        model = Advice
        fields = ['name','age','keywords']
# 'class':"form-control mt-2"
        # widgets={
        #     'name':forms.TextInput(
        #     attrs={'maxlength': '20',
        #            'size':'10',
        #            }
        #     )
        # }
        labels={
            'name':'이름',
            'keywords':'검색할 사진',
            'age':'나이'
        }



        # widgets={
        #     'searh_result_image':forms.ClearableFileInput(attrs={'multiple':True})
        # }


class UploadForm_1(forms.ModelForm):
    class Meta:
        model = Advice
        fields = ['name','age']
        labels={
            'name':'이름',
            'age':'나이'
        }


class uploadForm_2(forms.ModelForm):
    class Meta:
        model = SearchImage
        fields = ['search_image']

        labels={
            'search_image':'업로드',
          
        }