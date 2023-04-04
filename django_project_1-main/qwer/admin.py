from django.contrib import admin
from .models import Advice,AdviceImage



@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
    pass


    
@admin.register(AdviceImage)
class AdviceImageAdmin(admin.ModelAdmin):
    pass

