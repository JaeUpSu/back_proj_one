from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")
    is_business = models.BooleanField(default=True)    

# # Create your models here.
# class User(models.Model):
#     nickname = models.CharField(max_length=30)
#     phone = models.PositiveIntegerField()
#     is_business = models.BooleanField(default=False)
#     gender = models.CharField(max_length=10)
#     profileIntroduce = models.TextField(max_length=20) 
    
#     def __str__(self):
#         return str(self.pk)
    