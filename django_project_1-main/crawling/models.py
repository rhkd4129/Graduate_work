from django.db import models
from django.urls import reverse
from django.conf import settings
   
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
 

class ImageModel(models.Model):
    image = ProcessedImageField(
        upload_to='crawing/%Y/%m/%d',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 90}
    )

class Advice(models.Model):
    class GenderChices(models.TextChoices):
        MALE = "M","Male"   #DB에저장되는 값 ,실제 사용할 값
        FEMALE = "F","Female"
    customer = models.CharField(max_length=10)
    
    keyword = models.CharField(max_length=20)
    find_image_number = models.IntegerField()
    searh_result_image = models.FileField()

    #searh_result_image = models.ImageField(blank=True,upload_to='crawing/%Y/%m/%d')\
    #searh_result_image = models.ManyToManyField('ImageModel', blank=True)
    gender = models.CharField(max_length=1,blank=True,choices=GenderChices.choices)#,default=GenderChices.MALE  
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.keyword

    def get_absolute_url(self):
         return reverse('crawling:search_image')
