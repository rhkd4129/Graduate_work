from django.contrib import admin

from .models import Advice
from .forms import searchForm
@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    form = searchForm
    def save_model(self, request, obj, form, change):
        searh_result_image = request.FILES.getlist('searh_result_image')
        for f in searh_result_image:
            instance = Advice(searh_result_image=f)
# Register your models here.
