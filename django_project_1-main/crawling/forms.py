from django import forms



class searchForm(forms.Form):
    search = forms.CharField(label='Search')
    image_number = forms.IntegerField( min_value=1, max_value=10,label='number')