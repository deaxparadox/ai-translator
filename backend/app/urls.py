from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("team/", views.team, name="team"),
    path("aboutus/", views.aboutus, name="aboutus"),
]
