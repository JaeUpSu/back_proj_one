from django.urls import path
from . import views

urlpatterns = [
    # path("", views.show_user),
    path("myinfo", views.MyInfo.as_view())
]
