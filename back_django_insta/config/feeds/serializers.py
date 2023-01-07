from rest_framework.serializers import ModelSerializer
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer
from .models import Feed

class FeedsSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"
        depth = 1   # objects 도 serialize 화
        
    
class FeedListSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = ("id", "content", "like")
        
class FeedDetailSerializer(ModelSerializer):
    user = FeedUserSerializer()
    review_set = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Feed
        fields = "__all__"