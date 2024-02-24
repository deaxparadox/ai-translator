from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.http import (
    HttpResponse, 
    HttpResponseRedirect, 
    HttpResponsePermanentRedirect
)

from app.forms import UserRegisterForm, UserSignInForm


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
                return redirect(reverse("app:translate"))
        else:
            return create_signin_form(request)
    else:
        return create_signin_form(request)

def signout_view(request):
    logout(request)
    return redirect(reverse("app:signin"))



def create_register_form(request) -> HttpResponse:
    """
    Create the user registeration form, and return response
    """
    form = UserRegisterForm()
    return render(request, "register.html", {"form": form})


def register_view(request) -> (HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("app:signin"))
        else:
            print("Invalid register form")
            return create_register_form(request)
    return create_register_form(request)