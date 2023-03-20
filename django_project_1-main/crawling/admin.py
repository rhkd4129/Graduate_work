from django.contrib import admin

from .models import Advice

@admin.register(Advice)
class PostAdmin(admin.ModelAdmin):
    pass
# Register your models here.
