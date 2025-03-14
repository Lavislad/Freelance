from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from django.forms import TextInput, PasswordInput, CharField
from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'placeholder': 'Username'
            }),
            'password': PasswordInput(attrs={
                'placeholder': 'Password'
            })
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

    first_name = forms.CharField(empty_value='')
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
