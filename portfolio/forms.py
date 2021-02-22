from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
