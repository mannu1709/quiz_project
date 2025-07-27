from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control'
        }),
        label=''
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }),
        label=''
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control'
        }),
        label=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }),
        }
        labels = {
            'username': ''
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control'
        }),
        label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        }),
        label='')
