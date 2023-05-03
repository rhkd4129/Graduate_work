from django.db import models
import re
from django.conf import settings

from django.urls import reverse
from django.shortcuts import resolve_url

class Advice(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    keywords = models.CharField(max_length=10)
    age = models.IntegerField()
    
    # gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.keywords}"
        # return f"{self.user.username} - {self.keywords}"
    def get_absolute_url(self):
         return reverse('coloring:result',args=[self.pk])


import os
class AdviceImage(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE, related_name='a')
    image = models.ImageField(upload_to='advice_images/')
    trans_image = models.ImageField(null = True ,  upload_to='trans_images/')
    
    # def get_absulute_url(self):
    #     return reverse('qwer:trans_image_result',args=)

    def __str__(self):
        # return f"{self.advice.user.username} - {self.advice.keywords} - {self.id}"
        return f"{self.advice.keywords} - {self.id}"
    def get_filename(self):
        return os.path.basename(self.trans_image.name)
        #   {% for advice_image in advice.a.all %}
        #         <img src="  {{ advice_image.image.url }}" alt="">
        #         {% endfor %}