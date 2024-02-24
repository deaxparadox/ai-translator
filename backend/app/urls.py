from django.urls import path

from app import views
from app.views import auth as auth_view

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("team/", views.team, name="team"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("translate/", views.translate_view, name="translate"),
    path("token/", views.get_api_token_view, name="get_api_token"),
    path("signin/", auth_view.signin_view, name="signin"),
    path("signout/", auth_view.signout_view, name="signout"),
    path("register/", auth_view.register_view, name="register"),
]
