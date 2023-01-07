from django.db import models
from users.models import User
from commons.models import CommonModel

# Create your models here.
class Review(CommonModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    feed = models.ForeignKey("feeds.Feed", on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=120)
    like = models.PositiveIntegerField()
    reply = models.CharField(max_length=30)

    def __str__(self):
        return self.user.__str__()