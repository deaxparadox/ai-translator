from django.shortcuts import render, redirect
from django.urls import reverse
from django.http.response import JsonResponse
from django.contrib.auth.models import User

from app.models import LTSAPIToken

def dashboard_view(request):
    return render(request, "dashboard.html")

def index(request):
    # return render(request, "index.html")
    return redirect(reverse("app:dashboard"))


def team(request):
    return render(request, "down-time.html")



def aboutus(request):
    return render(request, "down-time.html")


def translate_view(request):
    return render(
        request,
        "translate.html"
    )

def get_api_token_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        return JsonResponse({'token': f'{user.ltsapitoken.token}'})
    return JsonResponse({
        "message": "User not authenticated."
    })