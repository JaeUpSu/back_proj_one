from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.show_feed),
#     path("<int:feed_id>/<str:content_name>/", views.show_one_feed),
#     path("search/<int:user_>/", views.show_search_feed),
#     path("all", views.show_all_feeds),
# ]

urlpatterns = [
    path("", views.Feeds.as_view()),
    path("<int:feed_id>", views.FeedDetail.as_view())
]
