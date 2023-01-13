from django.urls import path
from . import views

urlpatterns = [
    # path("", views.show_user),
    path("myinfo", views.MyInfo.as_view()),
    path("", views.Users.as_view()),
    path("login", views.Login.as_view()),
    path("logout", views.Logout.as_view()),
]
