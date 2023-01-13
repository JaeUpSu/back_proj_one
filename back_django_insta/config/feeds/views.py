# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Feed
# from .forms import FeedForm

# # Create your views here.
# def show_feed(request):
#     feed_list = Feed.objects.order_by('create_at')
#     context = {"feed_list":feed_list}
#     return render(request, 'feeds/feed_list.html', context)

# # http://.../feeds/feed_id
# def show_one_feed(request, feed_id, content_name):
#     # return HttpResponse(Feed.objects.get(id=feed_id).content)
#     return HttpResponse(f"Feed id is {feed_id} Content_name is {content_name}")

# # http://.../feeds/feed_id
# def show_search_feed(request, user_):
#     feeds = Feed.objects.filter(user = user_)
#     return render(request, "feeds.html"
#                         , {"datas":feeds, "title":"검색한 피드 데이터 결과입니다."})


# # http://.../feeds/feed_id
# def show_all_feeds(request):
#     # return HttpResponse(Feed.objects.get(id=feed_id).content)
#     feeds = Feed.objects.all()
#     return render(request, "feeds.html"
#                         , {"datas":feeds, "title":"전체 피드 데이터 입니다."})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Feed
from .serializers import FeedsSerializer, FeedDetailSerializer
class Feeds(APIView):
    
    def get(self, request):
        feeds = Feed.objects.all()
        print("feeds")
        print(feeds)
        
        serializer = FeedsSerializer(feeds, many=True)
        print("serializer")
        print(serializer)
        
        return Response(serializer.data)
    
    # def post(self, request):
    #    feed = request.feed => JSON
    #    feeds = Feed.objects.create(FeedsSerializer(feed))
        
    # def put(self, request):
    #     feed = request.feed => JSON
    #     feeds = Feed.objects.update(FeedsSerializer(feed))
        
    # def delete(self, request):
    #     JSON => ID값 뽑아서
    #     datas = Feed.objects.get(id=id)
        
        
class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, feed_id):
        feed = self.get_object(feed_id)
        serializer = FeedDetailSerializer(feed)
        return Response(serializer.data)
        









