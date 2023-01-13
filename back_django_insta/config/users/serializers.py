from rest_framework.serializers import ModelSerializer
from .models import User

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "is_business")
        
class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "is_superuser", "is_staff"
                   ,"is_active","first_name","last_name")