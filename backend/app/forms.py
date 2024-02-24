from typing import Any
from django.contrib.auth.models import User
from django.db import IntegrityError
from django import forms
from uuid import uuid4

from app.models import LTSAPIToken

class UserSignInForm(forms.Form):
    username = forms.CharField(
        label="Username",
        help_text="Enter your user name",
        required=True,
        widget=forms.TextInput,
    )
    
    password = forms.CharField(
        label="Password",
        help_text="Enter your password",
        required=True,
        widget=forms.PasswordInput
    )
    class Meta:
        fields = ["username", "password"]



class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        help_text="Enter your user name",
        required=True,
        widget=forms.TextInput
    )
    email = forms.CharField(
        label="Email",
        help_text="Enter your email",
        required=False,
        widget=forms.EmailInput
    )
    
    password = forms.CharField(
        label="Password",
        help_text="Enter your password",
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def _check_duplicate(self, token: str) -> bool:
        query_set = LTSAPIToken.objects.filter(token=token)
        if len(query_set) > 0:
            return False
        return True

    def save(self, *args, **kwargs) -> Any:
        token: str | None = None
        while True:
            token = str(uuid4())
            if self._check_duplicate(token):
                break
        try:
            user = User.objects.create(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        except User.MultipleObjectsReturned as e:
            print(e)
            return None
        except IntegrityError as e:
            print(e)
            return None

        instance = LTSAPIToken.objects.create(user=user, token=token)
        return instance