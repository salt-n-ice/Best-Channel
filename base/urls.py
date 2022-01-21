from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("regiser/", views.registerUser, name="register"),
    path("", views.home, name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room", views.createRoom, name="create-room"),
    path("profile/<str:pk>", views.userProfile, name="user-profile"),
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
    path("delete-message/<str:pk>", views.deleteMessage, name="delete-message"),
    path("update-user", views.updateUser, name="update-user"),
    path("upvote-room/<str:pk>", views.upvoteRoom, name="upvote-room"),
    path("unvote-room/<str:pk>", views.unvoteRoom, name="unvote-room"),
]
