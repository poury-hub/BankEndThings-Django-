from django.urls import path
from myapp import views

urlpatterns = [
    path("hellow/",views.hellow_world),
    path("welcome/",views.welcome),
]