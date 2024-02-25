from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import (
    HttpResponse, 
    HttpResponseRedirect, 
    HttpResponsePermanentRedirect,
    JsonResponse
)
from django.contrib import messages
import requests
import json

from app.forms import UserRegisterForm, UserSignInForm
from app import models


def create_signin_form(request) -> HttpResponse:
    """
    Create the user form, and return response
    """
    form = UserSignInForm()
    return render(request, "signin.html", {"form": form})

def signin_view(request) -> (HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect):
    if request.method == "POST":
        form = UserSignInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                messages.add_message(
                    request, messages.INFO,
                    "User successfully logged in."
                )
                return redirect(reverse("app:translate"))
            else: 
                messages.add_message(request, messages.INFO, "Invalid User")
                return create_signin_form(request)
        else:
            messages.add_message(request, messages.INFO, "Invalid Form")
            return create_signin_form(request)
    else:
        messages.add_message(request, messages.INFO, "User need to signin.")
        return create_signin_form(request)

def signout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, "User successfully logged out.")
    return redirect(reverse("app:signin"))



def create_register_form(request) -> HttpResponse:
    """
    Create the user registeration form, and return response
    """
    form = UserRegisterForm()
    return render(request, "register.html", {"form": form})

def register_create_token(request, token: str) -> bool:
    data = json.dumps({"token": token})
    print("\tSending requests for creating token")
    res = None
    try:
        res = requests.post("http://localhost:9000/user/create", data=data)
    except:
        messages.add_message(request, messages.INFO, "Unable to connect to register token")
        return False
    match res.status_code:
        case 201:
            print("\tToken created successfull")
            messages.add_message(request, messages.INFO, "Token created successfully :)")
            return True
        case 409:
            print("Unable to create token")
            messages.add_message(request, messages.INFO, f"Unable to create token :( {res.text}")
            return False
        case _:
            print("Unable to create token")
            messages.add_message(request, messages.INFO, f"Unable to create token :( {res.text}")
            return False

def register_view(request) -> (HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            token_object = form.save()
            if register_create_token(request, token_object.token):
                return redirect(reverse("app:signin"))
            else:
                token_object.delete()
                return create_register_form(request)
        else:
            print("Invalid register form")
            return create_register_form(request)
    return create_register_form(request)


def token_view(request) -> JsonResponse:
    if request.user.is_authenticated:
        user: User = User.objects.get(id=request.user.id)
        token: models.LTSAPIToken = models.LTSAPIToken.objects.get(user=user)
        return JsonResponse({"token": token.token})
    else:
        return JsonResponse({"error": "User not authenticated"})