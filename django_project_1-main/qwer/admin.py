from django.contrib import admin
from .models import Advice,AdviceImage



@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
      # list_display = ['pk','photo_tag','message','message_length','is_public','created_at','updated_at']
    list_display=['name','keywords','age','id']

    
@admin.register(AdviceImage)
class AdviceImageAdmin(admin.ModelAdmin):
    pass

