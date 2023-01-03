from django.db import models

# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=30)
    phone = models.PositiveIntegerField()
    is_business = models.BooleanField(default=False)
    gender = models.CharField(max_length=10)
    profileIntroduce = models.TextField(max_length=20) 
    
    def __str__(self):
        return str(self.pk)