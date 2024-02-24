from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
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
    # password2 = forms.CharField(
    #     label="Password Again",
    #     help_text="Enter your password again",
    #     required=True,
    #     widget=forms.PasswordInput
    # )
    class Meta:
        model = User
        fields = ["username", "email", "password"]