from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # phone_number = models.CharField(blank =True ,default='' ,max_length=12)
    pass

# Create your models here.