from django.urls import path

from . import views

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("team/", views.team, name="team"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("translate/", views.translate_view, name="translate"),
    path("token/", views.get_api_token_view, name="get_api_token"),
]
