from django.db import models

# Create your models here.
class CommonModel(models.Model):
    
    # ValidationError(DateTime format Error)
    # datetime.strptime(request.POST['date'], "%Y-%m-%dT%H:%M") 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    
    # 해당 모델을 DB로 쓰는게 아니라 추상화(기능)을 추가하겠다라는 의미
    class Meta:
        abstract = True
        
