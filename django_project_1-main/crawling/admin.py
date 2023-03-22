from django.contrib import admin

from .models import Advice
from .forms import searchForm
@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    # form = searchForm
    list_display = ['customer','keyword','find_image_number','searh_result_image','gender','created_at']
    def save_model(self, request, obj, form, change):
        searh_result_image = request.FILES.getlist('searh_result_image')
        for f in searh_result_image:
            instance = Advice(searh_result_image=f)
            instance.save()
            
# Register your models here.
