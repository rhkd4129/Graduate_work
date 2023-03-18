from django.urls import reverse
from django.db import models
from django.conf import settings


class Post(models.Model):
    class GenderChices(models.TextChoices):
        MALE = "M","Male"   #DB에저장되는 값 ,실제 사용할 값
        FEMALE = "F","Female"
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) # 추천!
    title = models.CharField(max_length=20)
    photo = models.ImageField(blank = True, upload_to = 'blog/post/%Y/%m/%d')
    content = models.TextField()
    gender = models.CharField(max_length=1,blank=True,choices=GenderChices.choices)#,default=GenderChices.MALE
    is_public = models.BooleanField(default = False,verbose_name= '공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title


    def get_absolute_url(self):
         return reverse('blog:post_detail',args=[self.pk])

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) # 추천!
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    message = models.CharField(max_length=200,help_text='200자 이하만')#related_name역참조 시 사용할모델
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.message

    class meta:
       ordering = ['-updated_at']
# Create your models here.
