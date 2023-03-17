from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['id','search_keyword','created_at',]
    list_display_links = ['search_keyword']
    search_fields = ['search_keyword']
#admin.site.register(Post)
