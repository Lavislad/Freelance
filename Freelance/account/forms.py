from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.forms import TextInput, PasswordInput


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