from django.urls import path

#!!!appname
from . import views

urlpatterns = [
    path("home/", views.home),
]
