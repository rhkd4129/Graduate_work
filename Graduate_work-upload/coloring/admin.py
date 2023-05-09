from django.contrib import admin
from .models import Advice,SearchImage,TransImage



@admin.register(Advice)
class AdviceAdmin(admin.ModelAdmin):
      # list_display = ['pk','photo_tag','message','message_length','is_public','created_at','updated_at']
    list_display=['name','keywords','age','id']

    

    
@admin.register(SearchImage)
class AdviceImageAdmin(admin.ModelAdmin):
    pass


    
@admin.register(TransImage)
class TransImageAdmin(admin.ModelAdmin):
    pass

