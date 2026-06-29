from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import BaseView, CreateRoomView,RegisterView,UserLoginView,UserLogoutView, PauseView, RoomView, RoomSearchView,PauseReturnView, VideoSaveView, TimeReturnView, TimeSaveView

urlpatterns = [
    path("",BaseView.as_view(),name="home"),
    path("<str:pk>/room/",RoomView.as_view(),name="room"),
    path("createroom/",CreateRoomView.as_view(),name="createroom"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("logout/",UserLogoutView.as_view(),name="logout"),
    path("register/",RegisterView.as_view(),name="register"),
    path("roomjoin/",RoomSearchView.as_view(),name="roomjoin"),
    path("<str:pk>/pause/",PauseView,name="pause"),
    path("<str:pk>/pausereturn/",PauseReturnView,name="pausereturn"),
    path("<str:pk>/videosave/",VideoSaveView,name="videosave"),
    path("<str:pk>/timereturn/",TimeReturnView,name="timereturn"),
    path("<str:pk>/timesave/",TimeSaveView,name="timesave"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)