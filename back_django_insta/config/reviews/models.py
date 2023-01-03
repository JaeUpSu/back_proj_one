from django.db import models
from users.models import User

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=120)
    like = models.DecimalField(max_digits=9, decimal_places=0)
    reply = models.CharField(max_length=30)
