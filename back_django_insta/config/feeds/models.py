from django.db import models
from users.models import User
from reviews.models import Review
from commons.models import CommonModel

# Create your models here.
class Feed(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    like = models.PositiveIntegerField()
    img = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.user.__str__()
