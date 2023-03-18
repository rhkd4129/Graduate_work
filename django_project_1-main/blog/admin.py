from django.contrib import admin
from .models import Post,Comment
from django.utils.safestring import mark_safe



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
    # list_display = ['pk','photo_tag','message','message_length','is_public','created_at','updated_at']
    # list_display_links = ['message']
    # search_fields =['message']
    # list_filter =['is_public']
    # def message_length(self,post):
    #     return len(post.message)

    # def photo_tag(self,post):
    #     if post.photo:
    #         return mark_safe(f'<img src = "{post.photo.url}" style="width:75px" /> ')
    #     return None

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass



# Register your models here.
