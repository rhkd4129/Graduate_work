from django.db import models


class Post(models.Model):
    search_keyword = models.CharField(max_length=15)
    image_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(blank = True)#upload_to = 'blog/post/%Y/%m/%d'