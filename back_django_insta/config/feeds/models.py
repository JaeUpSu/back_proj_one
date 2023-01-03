from django.db import models
from users.models import User

# Create your models here.
class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #reivew = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    like = models.DecimalField(max_digits=9, decimal_places=0)
    img = models.ImageField(blank=True, null=True)
    
    