from django.urls import path
from myApp import views

urlpatterns = [
    path("hello_world", views.hello_world),
    path("hell", views.hell),
]